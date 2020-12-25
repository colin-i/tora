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

def cmpval(byts):
	i=0
	a=len(byts)
	for x in mirror:
		x=x.value
		if a==len(x):
			j=0
			while x[j]==byts[j]:
				j=j+1
				if j==a:
					return i
		i=i+1
@gtk.CALLBACK3b
def forfnc(model,path,iter):
	val=gtk.c_char_p()
	byts=gtk.cast(k.gtk_tree_path_to_string(path),gtk.c_char_p)
	i=cmpval(byts.value)
	gtk.gtk_tree_model_get(model,torrent.torrents[i].it,layout.COLUMNS.UP,gtk.byref(val))
	k.g_free(byts)
	#
	name=gtk.c_char_p()#:gtk.c_char_p except UnboundLocalError
	path=gtk.c_char_p()
	gtk.gtk_tree_model_get2 (model, iter, layout.COLUMNS.NAME, gtk.byref(name), layout.COLUMNS.PATH, gtk.byref(path))
	dict={'name':name.value.decode(),'path':path.value.decode(),
		'upload':int(val.value.decode())}
	k.g_free(name)
	k.g_free(path)
	arr.append(dict)
	return False

def write(lst):
	global arr
	arr=[]
	global mirror
	mirror=[]
	for x in torrent.torrents:
		p=k.gtk_tree_model_get_path(lst,x.it)
		mirror.append(gtk.cast(k.gtk_tree_path_to_string(p),gtk.c_char_p))
		k.gtk_tree_path_free(p)
	k.gtk_tree_model_foreach(lst,forfnc)
	for s in mirror:
		k.g_free(s)
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
			gtk.gtk_list_store_set4(lst, ip, layout.COLUMNS.NAME, x['name'].encode(), layout.COLUMNS.PATH, p.encode(),
				layout.COLUMNS.UP,b"0",layout.COLUMNS.DOWN,b"0")
			torrent.open(p,ip,x['upload'])
	except Exception:
		pass
