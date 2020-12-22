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

def fresh():
	if stats.show(h):
		timer.cancel()

@gtk.CALLBACK
def download(tree):
	treesel.text0(start,tree)

def start(path):
	info = lt.torrent_info(path)
	p=k.gtk_entry_buffer_get_text(sets.fold_bf).decode("utf-8")
	global h
	h = ses.add_torrent({'ti': info, 'save_path': p})
	global timer
	timer=threading.Timer(5.0, fresh)
	timer.start()

def close():
	ses.remove_torrent(h)