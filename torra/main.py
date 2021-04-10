"""
torrent client
"""

import appdirs
import os.path
import pathlib
def get_root_dir():
	return pathlib.Path(appdirs.user_config_dir('torra'))
get_root_dir().mkdir(exist_ok=True)
def get_root_file(f):
	return os.path.join(get_root_dir(),f)

from . import gtk
from . import layout
from . import confs
from . import sets
from . import torrent
from . import overall
from . import listtor
from . import ratio
k=gtk.k

@gtk.CALLBACKi
def closing(window):
	listtor.write(layout.list)
	confs.write_opt(window)
	torrent.close()
	overall.close()
	ratio.freeint()
	return False

@gtk.CALLBACK
def activate(app):
	window = k.gtk_application_window_new (app)
	k.gtk_window_set_title (window, b"Torrent")
	k.g_signal_connect_data (window, b"close-request", closing, None, None, 0)
	k.gtk_widget_show (window)
	confs.read_opt(window)
	layout.layout(window)

def main():
	a=k.gtk_application_new(None,0)
	actv=b"activate"
	k.g_signal_connect_data (a, actv, activate, None, None, 0)
	r=k.g_application_run (a,0,None)
	k.g_object_unref(sets.fold_bf)
	k.g_object_unref(a)
	exit(r)

if __name__ == "__main__":
    main()
