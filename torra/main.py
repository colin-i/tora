"""
torrent client
"""

import sys

from . import confs
from . import gtk
from . import layout
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
	wd=confs.width
	if wd<0:
		confs.width=k.gtk_widget_get_width(window)
		if wd==-2:
			k.gtk_window_minimize(window)
	layout.layout(window)

def main():
	confs.get_root_dir().mkdir(exist_ok=True)

	if len(sys.argv)>1:
		listtor.config_filename=sys.argv[1]
	a=k.gtk_application_new(None,0)
	actv=b"activate"
	k.g_signal_connect_data (a, actv, activate, None, None, 0)
	r=k.g_application_run (a,0,None)
	k.g_object_unref(sets.fold_bf)
	k.g_object_unref(a)
	exit(r)

if __name__ == "__main__":
	main()
