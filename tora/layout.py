try:
	import gtk
	import addtor
	import listtor
except Exception:
	from . import gtk
	from . import addtor
	from . import listtor
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
	b=k.gtk_button_new_with_label(b"+")
	#
	k.gtk_box_append(bx,e)
	k.gtk_box_append(bx,b)
	#
	box=k.gtk_box_new(gtk.GtkOrientation.GTK_ORIENTATION_VERTICAL,0)
	scroll = k.gtk_scrolled_window_new ()
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
	k.g_signal_connect_data (b, b"clicked", add, e, None, gtk.GConnectFlags.G_CONNECT_SWAPPED)
	k.gtk_box_append(box,bx)
	k.gtk_box_append(box,scroll)
	k.gtk_window_set_child(window,box)