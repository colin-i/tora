import json
import os

import gtk
k=gtk.k
import layout

@gtk.CALLBACK3
def forfnc(model,path,iter):
	name=gtk.c_char_p()#:gtk.c_char_p except UnboundLocalError
	path=gtk.c_char_p()
	k.gtk_tree_model_get (model, iter, layout.COLUMNS.NAME, gtk.byref(name), layout.COLUMNS.PATH, gtk.byref(path), -1)
	dict={'name':name.value.decode("utf-8"),'path':path.value.decode("utf-8")}
	k.g_free(name)
	k.g_free(path)
	arr.append(dict)
	return False

def list(lst):
	global arr
	arr=[]
	k.gtk_tree_model_foreach(lst,forfnc)
	config_filename = os.path.join(os.path.dirname(os.path.realpath(__file__)),'config', 'data')
	with open(config_filename, "w") as write_file:
	    json.dump(arr, write_file)