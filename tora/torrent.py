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
han=[]
timer=None

class tor():
	def __init__(self,h,it):
		self.h=h
		self.it=it

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
	h=han[i].h

def sel(tree):
	treesel.position(pos,tree)

def open(path,it):
	info = lt.torrent_info(path)
	p=k.gtk_entry_buffer_get_text(sets.fold_bf).decode("utf-8")
	t=tor(ses.add_torrent({'ti': info, 'save_path': p}),k.gtk_tree_iter_copy(it))
	han.append(t)

def close():
	for x in han:
		ses.remove_torrent(x.h)
		k.gtk_tree_iter_free(x.it)
	if timer:
		timer.cancel()