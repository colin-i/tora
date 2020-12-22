try:
	import gtk
	import meninfo
	import torrent
except Exception:
	from . import gtk
	from . import meninfo
	from . import torrent
k=gtk.k

thnumber=0

@gtk.CALLBACK0b
def menutime():
	global thnumber
	k.gtk_widget_hide(menu)
	thnumber=0
	return False

@gtk.CALLBACK0
def click():
	global thnumber
	if ( thnumber != 0):
		k.g_source_remove(thnumber)
	thnumber=k.g_timeout_add(10000,menutime)#,NULL)
	k.gtk_widget_show(menu)

def ini(parent,tree):
	global menu
	menu=k.gtk_box_new(gtk.GtkOrientation.GTK_ORIENTATION_HORIZONTAL,0)
	uni=chr(0x2B07).encode()
	b=k.gtk_button_new_with_label(uni)
	k.g_signal_connect_data(b,b"clicked",torrent.download,tree,None,gtk.GConnectFlags.G_CONNECT_SWAPPED)
	k.gtk_box_append(menu,b)
	uni=chr(0x24D8).encode()
	b=k.gtk_button_new_with_label(uni)
	k.g_signal_connect_data(b,b"clicked",meninfo.act,tree,None,0)
	k.gtk_box_append(menu,b)
	k.gtk_box_append(parent,menu)
	k.gtk_widget_hide(menu)
	k.g_signal_connect_data(tree,b"row-activated",click,None,None,0)
	k.gtk_tree_view_set_activate_on_single_click(tree,True)
