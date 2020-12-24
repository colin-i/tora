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

@gtk.CALLBACK3b
def forfnc(model,path,iter):
	name=gtk.c_char_p()#:gtk.c_char_p except UnboundLocalError
	path=gtk.c_char_p()
	gtk.gtk_tree_model_get2 (model, iter, layout.COLUMNS.NAME, gtk.byref(name), layout.COLUMNS.PATH, gtk.byref(path))
	dict={'name':name.value.decode("utf-8"),'path':path.value.decode("utf-8")}
	k.g_free(name)
	k.g_free(path)
	arr.append(dict)
	return False

def write(lst):
	global arr
	arr=[]
	k.gtk_tree_model_foreach(lst,forfnc)
	with open(config_filename, "w") as write_file:
		json.dump(arr, write_file)

def read(lst):
	i=gtk.GtkTreeIter()
	ip=gtk.byref(i)
	try:
		with open(config_filename) as f:
			dat=json.load(f)
		for x in dat:
			k.gtk_list_store_append(lst,ip)
			p=x['path']
			gtk.gtk_list_store_set2(lst, ip, layout.COLUMNS.NAME, x['name'].encode(), layout.COLUMNS.PATH, p.encode())
			torrent.open(p,ip)
	except Exception:
		pass
