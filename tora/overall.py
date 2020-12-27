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
	timer=k.g_timeout_add(5000,fresh)
	return list

def st(a):
	return str(a).encode()
def div_ratio(a,b):
	if not b:
		return "0"
	n=a/b
	return st(n)

@gtk.CALLBACK0i
def fresh():
	up=0
	down=0
	i=gtk.GtkTreeIter()
	ir=gtk.byref(i)
	mod=layout.list
	b=k.gtk_tree_model_get_iter_first(mod,ir)
	while b:
		p=gtk.c_int()
		gtk.gtk_tree_model_get(mod,ir,layout.COLUMNS.INDEX,gtk.byref(p))
		tor=torrent.torrents[p.value]
		s=tor.h.status()
		u=tor.u+s.total_payload_upload#if pause this will be 0, all_time_upload
		d=s.total_done
		gtk.gtk_list_store_set3(mod,ir,layout.COLUMNS.UP,st(u),layout.COLUMNS.DOWN,st(d),layout.COLUMNS.RATIO,div_ratio(u,d))
		up+=u
		down+=d
		b=k.gtk_tree_model_iter_next(mod,ir)
	gtk.gtk_list_store_set3(list,it,layout.COLUMNS.UP,st(up),layout.COLUMNS.DOWN,st(down),layout.COLUMNS.RATIO,div_ratio(up,down))
	return True

def close():
	k.g_source_remove(timer)