import os
configs_filename = os.path.join(os.path.dirname(os.path.realpath(__file__)),'configs')
import json

try:
	import gtk
except Exception:
	from . import gtk
k=gtk.k

@gtk.CALLBACK
def write_opt(window):
	dict={}
	width=gtk.c_int()
	height=gtk.c_int()
	k.gtk_window_get_size (window, gtk.byref(width), gtk.byref(height))
	dict['max']=k.gtk_window_is_maximized(window)
	dict['width']=width.value
	dict['height']=height.value
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
	except Exception:
		pass
