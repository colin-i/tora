import json
import os

config_filename = os.path.join(os.path.dirname(os.path.realpath(__file__)),'config')
#in folder is ... (lib/python3.7/site-packages/) tora/config and ...tora/config

try:
	import gtk
	import layout
except Exception:
	from . import gtk
	from . import layout
k=gtk.k

@gtk.CALLBACK3b
def forfnc(model,path,iter):
	name=gtk.c_char_p()#:gtk.c_char_p except UnboundLocalError
	path=gtk.c_char_p()
	k.gtk_tree_model_get (model, iter, layout.COLUMNS.NAME, gtk.byref(name), layout.COLUMNS.PATH, gtk.byref(path), -1)
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
			a=x['name'].encode()
			k.gtk_list_store_set(lst, ip, layout.COLUMNS.NAME, a, layout.COLUMNS.PATH, x['path'].encode(), -1)
	except Exception:
		pass
