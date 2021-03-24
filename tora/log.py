import subprocess

from . import gtk
from . import torrent
from . import ratio
k=gtk.k

#in case config file is not yet created
log_bf=k.gtk_entry_buffer_new(None,-1)
end_bf=k.gtk_entry_buffer_new(None,-1)
f=None
in_ratio=0

def ini():
	grid = k.gtk_grid_new ()
	k.gtk_grid_attach(grid,ratio.text(b"Location"),0,0,1,1)
	k.gtk_grid_attach(grid,ratio.edit(log_bf),1,0,1,1)
	k.gtk_grid_attach(grid,ratio.text(b"External command when closing"),0,1,1,1)
	k.gtk_grid_attach(grid,ratio.edit(end_bf),1,1,1,1)
	fr=k.gtk_frame_new(b"Log File")
	k.gtk_frame_set_child(fr,grid)
	return fr

def store(d):
	d['log_file']=finish()
	d['log_end']=k.gtk_entry_buffer_get_text(end_bf).decode()
def restore(d):
	log=d['log_file']
	if len(log)>0:
		k.gtk_entry_buffer_set_text(log_bf,log.encode(),-1)
		global f
		f=open(log,"w")
	k.gtk_entry_buffer_set_text(end_bf,d['log_end'].encode(),-1)


def div_nr(a,b):
	if not b:
		return 0
	return a/b
def one(x,s):
	u=x.u+s.total_payload_upload#if pause this will be 0, all_time_upload
	return div_nr(u,s.total_done)
def rest1(x,s):
	r=one(x,s)
	f.write(str(r)+"|"+str(r-x.in_ratio)+"\n")
def rest2(ratio):
	f.write("@"+str(ratio)+"|"+str(ratio-in_ratio)+"\n")
	f.flush()
def add0(rat):
	if f:
		global in_ratio
		if not in_ratio:
			in_ratio=rat
		b=True
		f.write("\n")
		for x in torrent.torrents:
			s=x.h.status()
			if(torrent.checki(s)):
				b=False
				continue
			elif not hasattr(x,'in_ratio'):
				x.in_ratio=one(x,s)
			rest1(x,s)
		rest2(rat)
		if b:
			global add
			add=add1
def add1(rat):
	if f:
		f.write("\n")
		for x in torrent.torrents:
			s=x.h.status()
			rest1(x,s)
		rest2(rat)
def likenew():
	global add
	add=add0
def addT(path):
	if f:
		f.write(path+"\n")

def finish():
	global f
	if f:
		bts=k.gtk_entry_buffer_get_text(end_bf)
		if bts:
			c=bts.decode()
			z=subprocess.run(c,capture_output=True)
			f.write(str(z.stdout))
		f.close()
		f=None
	return k.gtk_entry_buffer_get_text(log_bf).decode()
def reset():
	d=finish()
	if len(d)>0:
		global f
		f=open(d,"a")
