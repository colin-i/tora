from . import gtk
from . import torben
from . import listtor
from . import conmenu
from . import sets
from . import confs
from . import stats
from . import torrent
from . import overall
from . import next
k=gtk.k

from enum import IntEnum
class COLUMNS(IntEnum):
	NAME=0
	PATH=1
	UP=2
	DOWN=3
	RATIO=4
	n=5

def columns_add(tree,n,i,w):
	renderer = k.gtk_cell_renderer_text_new()
	column = k.gtk_tree_view_column_new_with_attributes(n, renderer, b"text", i, None)
	k.gtk_tree_view_append_column(tree, column)
	k.gtk_tree_view_column_set_resizable(column,True)
	if(w>0):
		k.gtk_tree_view_column_set_fixed_width(column,w)
def columns(tree,w):#gtk_window_remembered_size is forcing *height=priv->height
	w=int(w/COLUMNS.n)
	columns_add(tree,b"Name",COLUMNS.NAME,w)
	columns_add(tree,b"Path",COLUMNS.PATH,w)
	columns_add(tree,b"Uploaded",COLUMNS.UP,w)
	columns_add(tree,b"Downloaded",COLUMNS.DOWN,w)
	columns_add(tree,b"Ratio",COLUMNS.RATIO,w)

colsdef=lambda:k.gtk_list_store_new(COLUMNS.n, gtk.G_TYPE_STRING, gtk.G_TYPE_STRING, gtk.G_TYPE_STRING, gtk.G_TYPE_STRING, gtk.G_TYPE_STRING)
list=colsdef()
sort=k.gtk_tree_model_sort_new_with_model(list)
k.g_object_unref(list)

@gtk.CALLBACK
def add(window):
	b=k.gtk_entry_get_buffer(entry_tor)
	t=k.gtk_entry_buffer_get_text(b)
	tx=t.decode()
	if torrent.open_tor(tx,0,window):
		tex=torben.name(tx)
		i=gtk.GtkTreeIter()
		ip=gtk.byref(i)
		if k.gtk_tree_model_iter_n_children(list,None)==0:
			next.ini(treeV)
		k.gtk_list_store_append(list,ip)
		gtk.gtk_list_store_set5(list, ip, COLUMNS.NAME, tex, COLUMNS.PATH, t,
			COLUMNS.UP,b"0",COLUMNS.DOWN,b"0",COLUMNS.RATIO,b"0")
		listtor.write(list)
def layout(window):
	bx=k.gtk_box_new(gtk.GtkOrientation.GTK_ORIENTATION_HORIZONTAL,0)
	global entry_tor
	entry_tor=k.gtk_entry_new()
	k.gtk_widget_set_hexpand(entry_tor,True)
	k.g_signal_connect_data (entry_tor, b"activate", add, window, None, gtk.GConnectFlags.G_CONNECT_SWAPPED)
	#
	k.gtk_box_append(bx,entry_tor)
	b=k.gtk_button_new_with_label(b"+")
	k.gtk_box_append(bx,b)
	k.g_signal_connect_data (b, b"clicked", add, window, None, gtk.GConnectFlags.G_CONNECT_SWAPPED)
	#
	b=k.gtk_button_new_with_label(chr(0x2699).encode())
	k.g_signal_connect_data (b, b"clicked", sets.sets, window, None, gtk.GConnectFlags.G_CONNECT_SWAPPED)
	k.gtk_box_append(bx,b)
	#
	k.gtk_tree_sortable_set_sort_column_id(sort,COLUMNS.NAME,gtk.GtkSortType.GTK_SORT_ASCENDING)
	global treeV
	treeV=k.gtk_tree_view_new_with_model(sort)
	k.g_object_unref(sort)
	columns(treeV,confs.width)
	listtor.read(list,window)
	if k.gtk_tree_model_iter_n_children(list,None)>0:
		next.ini(treeV)
	#
	scroll = k.gtk_scrolled_window_new ()
	k.gtk_widget_set_vexpand(scroll,True)
	k.gtk_scrolled_window_set_child (scroll,treeV)
	#
	lst=overall.ini(colsdef())
	tree=k.gtk_tree_view_new_with_model(lst)
	k.g_object_unref(lst)
	columns(tree,confs.width)
	k.gtk_tree_view_set_headers_visible(tree,False)
	#
	box=k.gtk_box_new(gtk.GtkOrientation.GTK_ORIENTATION_VERTICAL,0)
	k.gtk_box_append(box,bx)
	k.gtk_box_append(box,scroll)
	k.gtk_box_append(box,tree)
	stats.ini(box)
	conmenu.ini(box,treeV)
	#
	k.gtk_window_set_child(window,box)