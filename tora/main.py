
"""
comment
"""

import gtk
k=gtk.k

import layout

@gtk.CALLBACK
def activate(app):
	window = k.gtk_application_window_new (app)
	k.gtk_window_set_title (window, b"Torrent")
	layout.layout(window)
	k.gtk_widget_show (window)

def main():
	a=k.gtk_application_new(None,0)
	actv=b"activate"
	k.g_signal_connect_data (a, actv, activate, None, None, 0)
	r=k.g_application_run (a,0,None)
	k.g_object_unref(a)
	exit(r)

if __name__ == "__main__":
    main()
