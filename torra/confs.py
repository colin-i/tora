
import os.path
import appdirs
import pathlib
def get_root_dir():
	return pathlib.Path(appdirs.user_config_dir('torra'))
def get_root_file(f):
	return os.path.join(get_root_dir(),f)

import json

from . import gtk
from . import sets
from . import ratio
from . import next
from . import log
from . import cons
k=gtk.k

configs_filename = get_root_file('configs')

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
	#global width#used at columns
	try:
		with open(configs_filename) as f:
			dict=json.load(f)
			k.gtk_window_set_default_size(window,dict['width'],dict['height'])  #to comeback here from maximize
			k.gtk_test_widget_wait_for_draw(window)  #widget_get_width and maximize without this? no
			if dict['max']:
				k.gtk_window_maximize(window)

			#width=-2 if dict['min'] else -1
			if dict['min']:
				k.gtk_window_minimize(window)

			a=dict['download_folder'].encode()
			k.gtk_entry_buffer_set_text(sets.fold_bf,a,-1)
			ratio.restore(dict)
			next.restore(dict)
			log.restore(dict)
			cons.restore(dict)
	except Exception:
		pass
	#	width=0
