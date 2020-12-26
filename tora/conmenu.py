import threading

try:
	import gtk
	import meninfo
	import torrent
except Exception:
	from . import gtk
	from . import meninfo
	from . import torrent
k=gtk.k

timer=None

def menutime():
	global timer
	k.gtk_widget_hide(menu)
	timer=None

@gtk.CALLBACK
def click(tree):
	global timer
	if timer:
		timer.cancel()
	k.gtk_widget_show(menu)
	torrent.sel(tree)
	timer=threading.Timer(10.0, menutime)
	timer.start()

def ini(parent,tree):
	global menu
	menu=k.gtk_box_new(gtk.GtkOrientation.GTK_ORIENTATION_HORIZONTAL,0)
	uni=chr(0x24D8).encode()
	b=k.gtk_button_new_with_label(uni)
	k.g_signal_connect_data(b,b"clicked",meninfo.act,tree,None,0)
	k.gtk_box_append(menu,b)
	uni=chr(0x1F5D1).encode()
	b=k.gtk_button_new_with_label(uni)
	k.gtk_box_append(menu,b)
	k.gtk_box_append(parent,menu)
	k.gtk_widget_hide(menu)
	k.g_signal_connect_data(tree,b"row-activated",click,None,None,0)
	k.gtk_tree_view_set_activate_on_single_click(tree,True)
