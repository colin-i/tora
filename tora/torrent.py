import libtorrent as lt

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
timer=0

class tor():
	def __init__(self,h,u):
		self.h=h
		self.u=u

@gtk.CALLBACK0i
def fresh():
	stats.show(h)
	return True

def pos(i):
	global timer
	if timer>0:
		k.g_source_remove(timer)
	timer=k.g_timeout_add(5000, fresh, None)
	global h
	h=torrents[i].h

def sel(tree):
	treesel.position(pos,tree)

def open(path,u):
	info = lt.torrent_info(path)
	pv=k.gtk_entry_buffer_get_text(sets.fold_bf)
	th=ses.add_torrent({'ti': info, 'save_path': pv})
	for x in torrents:
		if x.h==th:
			return False
	t=tor(th,u)
	torrents.append(t)
	return True

def close():
	for x in torrents:
		ses.remove_torrent(x.h)
	if timer>0:
		k.g_source_remove(timer)

def remsel(i):
	global timer
	k.g_source_remove(timer)
	timer=0
	ses.remove_torrent(h)
	del torrents[i]