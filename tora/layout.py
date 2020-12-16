try:
	import gtk
	import addtor
	import listtor
	import conmenu
except Exception:
	from . import gtk
	from . import addtor
	from . import listtor
	from . import conmenu
k=gtk.k

from enum import IntEnum
class COLUMNS(IntEnum):
	NAME=0
	PATH=1
	N=2

list=k.gtk_list_store_new(COLUMNS.N, gtk.G_TYPE_STRING, gtk.G_TYPE_STRING)

@gtk.CALLBACK
def add(entr):
	b=k.gtk_entry_get_buffer(entr)
	t=k.gtk_entry_buffer_get_text(b)
	tex=addtor.add(t)
	i=gtk.GtkTreeIter()
	ip=gtk.byref(i)
	k.gtk_list_store_append(list,ip);
	k.gtk_list_store_set(list, ip, COLUMNS.NAME, tex, COLUMNS.PATH, t, -1)
	listtor.write(list)
def layout(window):
	bx=k.gtk_box_new(gtk.GtkOrientation.GTK_ORIENTATION_HORIZONTAL,0)
	e=k.gtk_entry_new()
	k.gtk_widget_set_hexpand(e,True)
	#
	k.gtk_box_append(bx,e)
	b=k.gtk_button_new_with_label(b"+")
	k.gtk_box_append(bx,b)
	k.g_signal_connect_data (b, b"clicked", add, e, None, gtk.GConnectFlags.G_CONNECT_SWAPPED)
	#
	b=k.gtk_button_new_with_label(chr(0x2699).encode())
	k.gtk_box_append(bx,b)
	#
	box=k.gtk_box_new(gtk.GtkOrientation.GTK_ORIENTATION_VERTICAL,0)
	scroll = k.gtk_scrolled_window_new ()
	k.gtk_widget_set_vexpand(scroll,True)
	#
	s=k.gtk_tree_model_sort_new_with_model(list)
	k.g_object_unref(list)
	k.gtk_tree_sortable_set_sort_column_id(s,COLUMNS.NAME,gtk.GtkSortType.GTK_SORT_ASCENDING)
	tree=k.gtk_tree_view_new_with_model(s)
	k.g_object_unref(s)
	#
	renderer = k.gtk_cell_renderer_text_new()
	column = k.gtk_tree_view_column_new_with_attributes("", renderer, b"text", COLUMNS.NAME, None)
	k.gtk_tree_view_append_column(tree, column)
	#
	renderer = k.gtk_cell_renderer_text_new()
	column = k.gtk_tree_view_column_new_with_attributes("", renderer, b"text", COLUMNS.PATH, None)
	k.gtk_tree_view_append_column(tree, column)
	#
	k.gtk_tree_view_set_headers_visible(tree,False)
	listtor.read(list)
	k.gtk_scrolled_window_set_child (scroll,tree)
	#
	k.gtk_box_append(box,bx)
	k.gtk_box_append(box,scroll)
	#
	conmenu.ini(box,tree)
	#
	k.gtk_window_set_child(window,box)