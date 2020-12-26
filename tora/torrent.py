import libtorrent as lt
import threading

try:
	import gtk
	import treesel
	import stats
	import sets
except Exception:
	from . import gtk
	from . import treesel
	from . import stats
	from . import sets
k=gtk.k

ses = lt.session()
ses.listen_on(6881, 6891)
torrents=[]
timer=None
appender=0

class tor():
	def __init__(self,h,ix,u):
		self.h=h
		self.ix=ix
		self.u=u

def timeon():
	global timer
	timer=threading.Timer(5.0, fresh)
	timer.start()

def fresh():
	stats.show(h)
	timeon()

def pos(i):
	if timer:
		timer.cancel()
	timeon()
	global h
	h=torrents[i].h

def sel(tree):
	treesel.position(pos,tree)

def open(path,u):
	global appender
	info = lt.torrent_info(path)
	p=k.gtk_entry_buffer_get_text(sets.fold_bf).decode()
	t=tor(ses.add_torrent({'ti': info, 'save_path': p}),appender,u)
	torrents.append(t)
	a=appender
	appender=appender+1
	return a

def close():
	for x in torrents:
		ses.remove_torrent(x.h)
	if timer:
		timer.cancel()