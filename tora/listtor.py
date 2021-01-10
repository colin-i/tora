import json
import os

config_filename = os.path.join(os.path.dirname(os.path.realpath(__file__)),'config')
#in folder is ... (lib/python3.7/site-packages/) tora/config and ...tora/config

try:
	import gtk
	import layout
	import torrent
except Exception:
	from . import gtk
	from . import layout
	from . import torrent
k=gtk.k

def write(lst):
	arr=[]
	val=gtk.c_char_p()
	name=gtk.c_char_p()#:gtk.c_char_p except UnboundLocalError
	path=gtk.c_char_p()
	i=gtk.GtkTreeIter()
	it=gtk.byref(i)
	b=k.gtk_tree_model_get_iter_first(lst,it)
	while b:
		gtk.gtk_tree_model_get3 (lst, it,
			layout.COLUMNS.NAME,gtk.byref(name),
			layout.COLUMNS.PATH, gtk.byref(path),
			layout.COLUMNS.UP,gtk.byref(val))
		d={'name':name.value.decode(),'path':path.value.decode(),
			'upload':int(val.value)}
		k.g_free(name)
		k.g_free(path)
		arr.append(d)
		b=k.gtk_tree_model_iter_next(lst,it)
	with open(config_filename, "w") as write_file:
		json.dump(arr, write_file)

def read(lst):
	i=gtk.GtkTreeIter()
	ip=gtk.byref(i)
	try:
		with open(config_filename) as f:
			dat=json.load(f)
	except Exception:
		return
	for x in dat:
		p=x['path']
		if torrent.open_tor(p,x['upload']):
			k.gtk_list_store_append(lst,ip)
			gtk.gtk_list_store_set5(lst, ip,
				layout.COLUMNS.NAME, x['name'].encode(),
				layout.COLUMNS.PATH, p.encode(),
				layout.COLUMNS.UP,b"0",layout.COLUMNS.DOWN,b"0",
				layout.COLUMNS.RATIO,b"0")
