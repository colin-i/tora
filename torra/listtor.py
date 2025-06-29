import json

from . import confs
from . import gtk
from . import layout
from . import torrent
from . import torben
k=gtk.k
k2=gtk.k2

config_filename = confs.get_root_file('config')
#in folder is ... (lib/python3.7/site-packages/) tora/config and ...tora/config

def write(lst):
	arr=[]
	val=gtk.c_char_p()
	path=gtk.c_char_p()#:gtk.c_char_p except UnboundLocalError
	i=gtk.GtkTreeIter()
	it=gtk.byref(i)
	b=k.gtk_tree_model_get_iter_first(lst,it)
	while b:
		gtk.gtk_tree_model_get2 (lst, it,
			layout.COLUMNS.PATH, gtk.byref(path),
			layout.COLUMNS.UP,gtk.byref(val))
		d={'path':path.value.decode(),'upload':int(val.value)}
		k2.g_free(path)
		arr.insert(0,d)
		b=k.gtk_tree_model_iter_next(lst,it)
	with open(config_filename, "w") as write_file:
		json.dump(arr, write_file)

def read(lst,window):
	i=gtk.GtkTreeIter()
	ip=gtk.byref(i)
	try:
		with open(config_filename) as f:
			dat=json.load(f)
	except Exception:
		return
	for x in dat:
		p=x['path']
		if torrent.open_tor(p,x['upload'],window):
			k.gtk_list_store_prepend(lst,ip)
			gtk.gtk_list_store_set5(lst, ip,
				layout.COLUMNS.NAME, torben.name(p),
				layout.COLUMNS.PATH, p.encode(),
				layout.COLUMNS.UP,b"0",layout.COLUMNS.DOWN,b"0",
				layout.COLUMNS.RATIO,b"0")
