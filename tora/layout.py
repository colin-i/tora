try:
	import gtk
	import addtor
	import listtor
	import conmenu
	import sets
	import confs
except Exception:
	from . import gtk
	from . import addtor
	from . import listtor
	from . import conmenu
	from . import sets
	from . import confs
k=gtk.k

from enum import IntEnum
class COLUMNS(IntEnum):
	NAME=0
	PATH=1
	N=2

def columns(tree,w):
	renderer = k.gtk_cell_renderer_text_new()
	column = k.gtk_tree_view_column_new_with_attributes(b"Name", renderer, b"text", COLUMNS.NAME, None)
	k.gtk_tree_view_append_column(tree, column)
	k.gtk_tree_view_column_set_resizable(column,True)
	if(w>0):
		k.gtk_tree_view_column_set_fixed_width(column,w)
	#
	renderer = k.gtk_cell_renderer_text_new()
	column = k.gtk_tree_view_column_new_with_attributes(b"Path", renderer, b"text", COLUMNS.PATH, None)
	k.gtk_tree_view_append_column(tree, column)
	k.gtk_tree_view_column_set_resizable(column,True)
	if(w>0):
		k.gtk_tree_view_column_set_fixed_width(column,w)
colsdef=lambda:k.gtk_list_store_new(COLUMNS.N, gtk.G_TYPE_STRING, gtk.G_TYPE_STRING)
list=colsdef()

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
	k.g_signal_connect_data (b, b"clicked", sets.sets, window, None, gtk.GConnectFlags.G_CONNECT_SWAPPED)
	k.gtk_box_append(bx,b)
	#
	width=int(confs.width/2)#gtk_window_remembered_size is forcing *height=priv->height
	#
	s=k.gtk_tree_model_sort_new_with_model(list)
	k.g_object_unref(list)
	k.gtk_tree_sortable_set_sort_column_id(s,COLUMNS.NAME,gtk.GtkSortType.GTK_SORT_ASCENDING)
	treeV=k.gtk_tree_view_new_with_model(s)
	k.g_object_unref(s)
	columns(treeV,width)
	listtor.read(list)
	#
	scroll = k.gtk_scrolled_window_new ()
	k.gtk_widget_set_vexpand(scroll,True)
	k.gtk_scrolled_window_set_child (scroll,treeV)
	#
	overall=colsdef()
	tree=k.gtk_tree_view_new_with_model(overall)
	k.g_object_unref(overall)
	columns(tree,width)
	k.gtk_tree_view_set_headers_visible(tree,False)
	#
	box=k.gtk_box_new(gtk.GtkOrientation.GTK_ORIENTATION_VERTICAL,0)
	k.gtk_box_append(box,bx)
	k.gtk_box_append(box,scroll)
	k.gtk_box_append(box,tree)
	#
	conmenu.ini(box,tree)
	#
	k.gtk_window_set_child(window,box)