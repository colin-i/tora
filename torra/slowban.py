import libtorrent as lt

from . import gtk
from . import torrent
from . import ratio
k=gtk.k
k2=gtk.k2
k3=gtk.k3

import os
verbose=os.environ.get('verbose')
if verbose:
	print("slowban will be verbose")

#https://webtorrent.io/torrents/sintel.torrent
#libtorrent.torrent_info('sintel.torrent').total_size()

rate_default=0
interval_default=30
bottom_default=True
rate_bf=k.gtk_entry_buffer_new(str(rate_default).encode(),-1)                  #min down B/s per peer, 0=disabled
interval_bf=k.gtk_entry_buffer_new(str(interval_default).encode(),-1) #seconds between checks
bottom_val=bottom_default

timer=0
filt=lt.ip_filter()
banned=set()   #ip strings already banned this session

def getrate():
	return int(k.gtk_entry_buffer_get_text(rate_bf))
def getinterval():
	return int(k.gtk_entry_buffer_get_text(interval_bf))

@gtk.CALLBACK2
def bottom_toggled(btn,user_data):
	global bottom_val
	bottom_val=bool(k.gtk_check_button_get_active(btn))

def ban(ip):
	if ip in banned:
		return
	banned.add(ip)
	if verbose:
		print("slowban: banning "+ip)

	filt.add_rule(ip,ip,1)   #1 = blocked (ip_filter.blocked isn't exposed as a named attribute on this build)
	#0 = normal/unblocked, 1 = blocked , in ip_filter::access_flags , https://www.libtorrent.org/reference-Filter.html

	torrent.ses.set_ip_filter(filt)

@gtk.CALLBACK0i
def slowban():
	th=getrate()
	if th<=0:
		return True
	for t in torrent.torrents:
		h=t.h
		if not h.is_valid():
			continue
		try:
			peers=h.get_peer_info()
		except Exception:
			continue
		for p in peers:
			ip=p.ip[0]
			if ip in banned:
				continue
			#https://libtorrent.org/reference-Core.html , "They are given in bytes per second"
			if bottom_val and p.down_speed==0:
				continue
			if p.down_speed<th:
				ban(ip)
	return True

def stop():
	global timer
	if timer>0:
		k2.g_source_remove(timer)
		timer=0
def start():
	stop()
	global timer
	n=getinterval()
	if n>0:
		timer=k2.g_timeout_add(n*1000,slowban,None)

def store(d):
	d['slowban_rate']=getrate()
	d['slowban_interval']=getinterval()
	d['slowban_bottom']=bottom_val
def restore(d):
	k.gtk_entry_buffer_set_text(rate_bf,str(d.get('slowban_rate',rate_default)).encode(),-1)
	k.gtk_entry_buffer_set_text(interval_bf,str(d.get('slowban_interval',interval_default)).encode(),-1)

	global bottom_val
	bottom_val=bool(d.get('slowban_bottom',bottom_default))

	start()

def ini():
	grid=k.gtk_grid_new()
	k.gtk_grid_attach(grid,ratio.text(b"Min download B/s per peer (0 disable)"),0,0,1,1)
	k.gtk_grid_attach(grid,ratio.edit(rate_bf),1,0,1,1)
	k.gtk_grid_attach(grid,ratio.text(b"Check interval, seconds"),0,1,1,1)
	k.gtk_grid_attach(grid,ratio.edit(interval_bf),1,1,1,1)

	cb=k.gtk_check_button_new_with_label(b"Do not ban 0 B/s peers in this timeout") #(already handled by libtorrent) ?
	k.gtk_check_button_set_active(cb,bottom_val)
	k3.g_signal_connect_data(cb,b"toggled",bottom_toggled,None,None,0)
	k.gtk_grid_attach(grid,cb,0,2,2,1)

	fr=k.gtk_frame_new(b"Auto-ban slow peers (session only, cleared on restart)")
	k.gtk_frame_set_child(fr,grid)
	return fr
