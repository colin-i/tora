import os.path

from . import gtk
from . import layout
from . import torrent
from . import bencod
from . import sets
k=gtk.k

i=gtk.GtkTreeIter()
it=gtk.byref(i)

def ini(lst):
	global list
	list=lst
	k.gtk_list_store_append(list,it)
	global timer
	timer=k.g_timeout_add(5000,fresh,None)
	return list

def st(a):
	return str(a).encode()
def div_ratio(a,b):
	if not b:
		return "0"
	n=a/b
	return st(n)

def download_sz(mod,ir):
	item_text=gtk.c_char_p()
	gtk.gtk_tree_model_get (mod, ir, layout.COLUMNS.PATH, gtk.byref(item_text))
	val=item_text.value.decode()
	k.g_free(item_text)
	size=0
	try:
		with open(val,'rb') as f:
			dldir=k.gtk_entry_buffer_get_text(sets.fold_bf).decode()
			#join can concat bytes,but unicode decode otherwise filenotfound
			#	p.s. join cannot mix str and bytes
			d=f.read()
			cod=bencod.decode(d)
			infs=cod[0][b'info']
			fl=infs[b'name'].decode()
			if b'files' in infs:
				files=infs[b'files']
				dldir=os.path.join(dldir,fl)
				for x in files:
					p=x[b'path']
					nm=dldir
					for y in p:
						nm=os.path.join(nm,y.decode())
					size+=os.path.getsize(nm)
			else:
				size=os.path.getsize(os.path.join(dldir,fl))
	except Exception:
		pass
	return size

@gtk.CALLBACK0i
def fresh():
	up=0
	down=0
	i=gtk.GtkTreeIter()
	ir=gtk.byref(i)
	mod=layout.list
	b=k.gtk_tree_model_get_iter_first(mod,ir)
	j=0
	while b:
		tor=torrent.torrents[j]
		h=tor.h
		s=h.status()
		u=tor.u+s.total_payload_upload#if pause this will be 0, all_time_upload
		if torrent.checki(s):
			d=download_sz(mod,ir)
		else:
			d=s.total_done
		gtk.gtk_list_store_set3(mod,ir,layout.COLUMNS.UP,st(u),layout.COLUMNS.DOWN,st(d),layout.COLUMNS.RATIO,div_ratio(u,d))
		up+=u
		down+=d
		b=k.gtk_tree_model_iter_next(mod,ir)
		j+=1
	gtk.gtk_list_store_set3(list,it,layout.COLUMNS.UP,st(up),layout.COLUMNS.DOWN,st(down),layout.COLUMNS.RATIO,div_ratio(up,down))
	return True

def close():
	k.g_source_remove(timer)