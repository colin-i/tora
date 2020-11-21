import gtk
k=gtk.k

from enum import IntEnum
class COLUMNS(IntEnum):
      NAME=0
      N=1

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
	tree=k.gtk_tree_view_new()
	renderer = k.gtk_cell_renderer_text_new()
	column = k.gtk_tree_view_column_new_with_attributes("", renderer, b"text", COLUMNS.NAME, None)
	k.gtk_tree_view_append_column(tree, column)
	k.gtk_tree_view_set_headers_visible(tree,False)
	ls=k.gtk_list_store_new(COLUMNS.N, gtk.G_TYPE_STRING, gtk.G_TYPE_STRING)
	k.gtk_tree_view_set_model(tree, ls)
	k.g_object_unref(ls)
	k.gtk_scrolled_window_set_child (scroll,tree)
	#
	k.gtk_box_append(box,bx)
	k.gtk_box_append(box,scroll)
	k.gtk_window_set_child(window,box)