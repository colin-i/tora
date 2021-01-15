import os
configs_filename = os.path.join(os.path.dirname(os.path.realpath(__file__)),'configs')
import json

try:
	from . import gtk
	from . import sets
	from . import ratio
	from . import next
	from . import log
except Exception:
	import gtk
	import sets
	import ratio
	import next
	import log
k=gtk.k

def write_opt(window):
	dict={}
	width=gtk.c_int()
	height=gtk.c_int()
	k.gtk_window_get_default_size (window, gtk.byref(width), gtk.byref(height))
	dict['max']=k.gtk_window_is_maximized(window)
	dict['width']=width.value
	dict['height']=height.value
	dict['min']=k.gdk_toplevel_get_state(k.gtk_native_get_surface(window))&gtk.GdkToplevelState.GDK_TOPLEVEL_STATE_MINIMIZED
	#
	dict['download_folder']=k.gtk_entry_buffer_get_text(sets.fold_bf).decode()
	ratio.store(dict)
	next.store(dict)
	log.store(dict)
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
			if dict['min']:
				k.gtk_window_minimize(window)
			#
			a=dict['download_folder'].encode()
			k.gtk_entry_buffer_set_text(sets.fold_bf,a,-1)
			ratio.restore(dict)
			next.restore(dict)
			log.restore(dict)
	except Exception:
		width=0
	ratio.newint(window)
