import libtorrent as lt

try:
	import gtk
	import treesel
	import stats
	import sets
	import layout
except Exception:
	from . import gtk
	from . import treesel
	from . import stats
	from . import sets
	from . import layout
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

def open_tor(path,u):
	try:
		with open(path+".fastresume") as f:
			b=f.read()
			c=eval(b)
			d=lt.bencode(c)
			td=lt.read_resume_data(d)
	except Exception:
		info = lt.torrent_info(path)
		pv=k.gtk_entry_buffer_get_text(sets.fold_bf)
		td={'ti': info, 'save_path': pv}
	th=ses.add_torrent(td)
	for x in torrents:
		if x.h==th:
			return False
	t=tor(th,u)
	torrents.append(t)
	return True

def close():
	if timer>0:
		k.g_source_remove(timer)
	i=gtk.GtkTreeIter()
	it=gtk.byref(i)
	mod=layout.list
	item_text=gtk.c_char_p()
	b=k.gtk_tree_model_get_iter_first(mod,it)
	j=0
	while b:
		gtk.gtk_tree_model_get (mod, it, layout.COLUMNS.PATH, gtk.byref(item_text))
		th=torrents[j].h
		with open(item_text.value.decode()+".fastresume", "w") as f:
			f.write(str(th.write_resume_data()))
		ses.remove_torrent(th)
		b=k.gtk_tree_model_iter_next(mod,it)
		j+=1

def remsel(i):
	global timer
	k.g_source_remove(timer)
	timer=0
	ses.remove_torrent(h)
	del torrents[i]