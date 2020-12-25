import threading

try:
	import gtk
	import layout
	import torrent
except Exception:
	from . import gtk
	from . import layout
	from . import torrent
k=gtk.k

i=gtk.GtkTreeIter()
it=gtk.byref(i)

def ini(lst):
	global list
	list=lst
	k.gtk_list_store_append(list,it)
	global timer
	timer=threading.Timer(5.0, fresh)
	timer.start()
	return list

def st(a):
	return str(a).encode()
def div_ratio(a,b):
	if not b:
		return "0"
	n=a/b
	return st(n)

def fresh():
	up=0
	down=0
	for tor in torrent.torrents:
		s=tor.h.status()
		u=tor.u+s.total_upload
		d=s.total_download
		gtk.gtk_list_store_set3(layout.list,tor.it,layout.COLUMNS.UP,st(u),layout.COLUMNS.DOWN,st(d),layout.COLUMNS.RATIO,div_ratio(u,d))
		up+=u
		down+=d
	gtk.gtk_list_store_set3(list,it,layout.COLUMNS.UP,st(up),layout.COLUMNS.DOWN,st(down),layout.COLUMNS.RATIO,div_ratio(up,down))

def close():
	timer.cancel()