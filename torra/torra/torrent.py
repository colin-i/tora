import libtorrent as lt

from . import gtk
from . import stats
from . import sets
from . import layout
from . import log
from . import ratio
k=gtk.k

ses = lt.session()
ses.listen_on(6881, 6891)
torrents=[]
timer=0

class tor():
	def __init__(self,h,u):
		self.h=h
		self.u=u

d_m='downloading metadata'.encode()
ckf='checking fastresume'.encode()
ck='checking'.encode()
state_str = ['queued'.encode(), \
	ck, d_m, 'downloading'.encode(), 'finished'.encode(), 'seeding'.encode(), \
	'allocating'.encode(), \
	ckf]
#queued and allocating are unused_enum_for_backwards_compatibility
#status().state.__int__() vs keys
#d meta
#chec fast,checking
#down,finish,sd
checki_states=[state_str.index(d_m),state_str.index(ckf),state_str.index(ck)]
def checki(s):
	for x in checki_states:
		if s.state==x:
			return True
	return False

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

def sel(tree,path):
	p2=k.gtk_tree_model_sort_convert_path_to_child_path(layout.sort,path)
	ix=k.gtk_tree_path_get_indices ( p2 )
	ix=ix[0]
	k.gtk_tree_path_free(p2)
	pos(ix)

def open_tor(path,u,w):
	try:
		with open(path+".fastresume") as f:
			b=f.read()
			c=eval(b)
			d=lt.bencode(c)
			td=lt.read_resume_data(d)
	except Exception:
		try:
			info = lt.torrent_info(path)
			pv=k.gtk_entry_buffer_get_text(sets.fold_bf)
			td={'ti': info, 'save_path': pv}
		except Exception:
			#the path is not existent
			print("Errors with: "+path)
			return False
	th=ses.add_torrent(td)#got no Name right after opening with libtor
	for x in torrents:
		if x.h==th:
			return False
	t=tor(th,u)
	torrents.insert(0,t)
	ratio.gain(w)
	log.addT(path)
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