
import json

from . import gtk
from . import sets
from . import ratio
from . import next
from . import log
from . import cons
from . import main
k=gtk.k

configs_filename = main.get_root_file('configs')

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
	cons.store(dict)
	with open(configs_filename, "w") as write_file:
		json.dump(dict, write_file)

def read_opt(window):
	global width#used at columns
	try:
		with open(configs_filename) as f:
			dict=json.load(f)
			if dict['max']:
				k.gtk_window_maximize(window)
				disp=k.gdk_display_get_default()
				mon=k.gdk_display_get_monitor_at_surface(disp,k.gtk_native_get_surface(window))
				rct=gtk.GdkRectangle()
				k.gdk_monitor_get_geometry(mon,gtk.byref(rct))
				width=rct.width
			else:
				k.gtk_window_set_default_size(window,width,dict['height'])
				width=dict['width']
			if dict['min']:
				k.gtk_window_minimize(window)
			#
			a=dict['download_folder'].encode()
			k.gtk_entry_buffer_set_text(sets.fold_bf,a,-1)
			ratio.restore(dict)
			next.restore(dict)
			log.restore(dict)
			cons.restore(dict)
	except Exception:
		width=0
