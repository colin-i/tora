import os
configs_filename = os.path.join(os.path.dirname(os.path.realpath(__file__)),'configs')
import json

try:
	import gtk
	import sets
	import ratio
	import next
except Exception:
	from . import gtk
	from . import sets
	from . import ratio
	from . import next
k=gtk.k

def write_opt(window):
	dict={}
	width=gtk.c_int()
	height=gtk.c_int()
	k.gtk_window_get_default_size (window, gtk.byref(width), gtk.byref(height))
	dict['max']=k.gtk_window_is_maximized(window)
	dict['width']=width.value
	dict['height']=height.value
	dict['download_folder']=k.gtk_entry_buffer_get_text(sets.fold_bf).decode()
	ratio.store(dict)
	next.store(dict)
	with open(configs_filename, "w") as write_file:
	    json.dump(dict, write_file)

def read_opt(window):
	global width#used at columns
	try:
		with open(configs_filename) as f:
			dict=json.load(f)
			if dict['max']:
				width=0
				k.gtk_window_maximize(window)
			else:
				width=dict['width']
				k.gtk_window_set_default_size(window,width,dict['height'])
			a=dict['download_folder'].encode()
			k.gtk_entry_buffer_set_text(sets.fold_bf,a,-1)
			ratio.restore(dict)
			next.restore(dict)
	except Exception:
		width=0
	ratio.newint(window)
