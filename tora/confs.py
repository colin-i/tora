import os
configs_filename = os.path.join(os.path.dirname(os.path.realpath(__file__)),'configs')
import json

try:
	import gtk
	import sets
except Exception:
	from . import gtk
	from . import sets
k=gtk.k

@gtk.CALLBACK
def write_opt(window):
	dict={}
	width=gtk.c_int()
	height=gtk.c_int()
	k.gtk_window_get_default_size (window, gtk.byref(width), gtk.byref(height))
	dict['max']=k.gtk_window_is_maximized(window)
	dict['width']=width.value
	dict['height']=height.value
	dict['download_folder']=k.gtk_entry_buffer_get_text(sets.fold_bf).decode("utf-8")
	with open(configs_filename, "w") as write_file:
	    json.dump(dict, write_file)

def read_opt(window):
	try:
		with open(configs_filename) as f:
			dict=json.load(f)
			if dict['max']:
				k.gtk_window_maximize(window)
			else:
				k.gtk_window_set_default_size(window,dict['width'],dict['height'])
			a=dict['download_folder'].encode()
			k.gtk_entry_buffer_set_text(sets.fold_bf,a,-1)
	except Exception:
		pass
