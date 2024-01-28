import libtorrent as lt

from . import gtk
from . import torrent
k=gtk.k

from enum import IntEnum
class COLUMNS(IntEnum):
	progress=0
	download_rate=1
	upload_rate=2
	num_peers=3
	state=4
	N=5
class COLUMNS2(IntEnum):
	list_peers=0
	num_complete=1
	num_incomplete=2
	next_announce=3
	last_upload=4
	N=5

#this is violation
#arr =  [24,64]
#arr_c = (gtk.c_int * 2)(*arr)
#k.gtk_list_store_newv.argtypes = [gtk.c_int, gtk.POINTER(gtk.c_int)]
#list=k.gtk_list_store_newv(gtk.c_int(2),arr_c)

#k.gtk_list_store_new is limited to 5 (five) entries, at six is violation

list=k.gtk_list_store_new(COLUMNS.N, gtk.G_TYPE_INT, gtk.G_TYPE_STRING, gtk.G_TYPE_STRING, gtk.G_TYPE_STRING, gtk.G_TYPE_STRING)
i=gtk.GtkTreeIter()
ip=gtk.byref(i)
k.gtk_list_store_append(list,ip)

list2=k.gtk_list_store_new(COLUMNS2.N, gtk.G_TYPE_STRING, gtk.G_TYPE_STRING, gtk.G_TYPE_STRING, gtk.G_TYPE_STRING, gtk.G_TYPE_STRING)
i2=gtk.GtkTreeIter()
ip2=gtk.byref(i2)
k.gtk_list_store_append(list2,ip2)

def ini(box):
	tree=k.gtk_tree_view_new_with_model(list)
	k.g_object_unref(list)
	renderer = k.gtk_cell_renderer_progress_new()
	column = k.gtk_tree_view_column_new_with_attributes(b"Percentage", renderer, b"value", COLUMNS.progress, None)
	k.gtk_tree_view_column_set_resizable(column,True)
	k.gtk_tree_view_column_set_expand(column,True)
	k.gtk_tree_view_append_column(tree, column)
	renderer = k.gtk_cell_renderer_text_new()
	column = k.gtk_tree_view_column_new_with_attributes(b"Download kB/s", renderer, b"text", COLUMNS.download_rate, None)
	k.gtk_tree_view_column_set_resizable(column,True)
	k.gtk_tree_view_column_set_expand(column,True)
	k.gtk_tree_view_append_column(tree, column)
	renderer = k.gtk_cell_renderer_text_new()
	column = k.gtk_tree_view_column_new_with_attributes(b"Upload kB/s", renderer, b"text", COLUMNS.upload_rate, None)
	k.gtk_tree_view_column_set_resizable(column,True)
	k.gtk_tree_view_column_set_expand(column,True)
	k.gtk_tree_view_append_column(tree, column)
	renderer = k.gtk_cell_renderer_text_new()
	column = k.gtk_tree_view_column_new_with_attributes(b"Peers num", renderer, b"text", COLUMNS.num_peers, None)
	k.gtk_tree_view_column_set_resizable(column,True)
	k.gtk_tree_view_column_set_expand(column,True)
	k.gtk_tree_view_append_column(tree, column)
	renderer = k.gtk_cell_renderer_text_new()
	column = k.gtk_tree_view_column_new_with_attributes(b"State", renderer, b"text", COLUMNS.state, None)
	k.gtk_tree_view_column_set_resizable(column,True)
	k.gtk_tree_view_column_set_expand(column,True)
	k.gtk_tree_view_append_column(tree, column)
	k.gtk_box_append(box,tree)
	#
	tree2=k.gtk_tree_view_new_with_model(list2)
	k.g_object_unref(list2)
	renderer = k.gtk_cell_renderer_text_new()
	column = k.gtk_tree_view_column_new_with_attributes(b"Peers list", renderer, b"text", COLUMNS2.list_peers, None)
	k.gtk_tree_view_column_set_resizable(column,True)
	k.gtk_tree_view_column_set_expand(column,True)
	k.gtk_tree_view_append_column(tree2, column)
	renderer = k.gtk_cell_renderer_text_new()
	column = k.gtk_tree_view_column_new_with_attributes(b"Seeds", renderer, b"text", COLUMNS2.num_complete, None)
	k.gtk_tree_view_column_set_resizable(column,True)
	k.gtk_tree_view_column_set_expand(column,True)
	k.gtk_tree_view_append_column(tree2, column)
	renderer = k.gtk_cell_renderer_text_new()
	column = k.gtk_tree_view_column_new_with_attributes(b"Leeches", renderer, b"text", COLUMNS2.num_incomplete, None)
	k.gtk_tree_view_column_set_resizable(column,True)
	k.gtk_tree_view_column_set_expand(column,True)
	k.gtk_tree_view_append_column(tree2, column)
	renderer = k.gtk_cell_renderer_text_new()
	column = k.gtk_tree_view_column_new_with_attributes(b"Next Announce", renderer, b"text", COLUMNS2.next_announce, None)
	k.gtk_tree_view_column_set_resizable(column,True)
	k.gtk_tree_view_column_set_expand(column,True)
	k.gtk_tree_view_append_column(tree2, column)
	renderer = k.gtk_cell_renderer_text_new()
	column = k.gtk_tree_view_column_new_with_attributes(b"Last Upload", renderer, b"text", COLUMNS2.last_upload, None)
	k.gtk_tree_view_column_set_resizable(column,True)
	k.gtk_tree_view_column_set_expand(column,True)
	k.gtk_tree_view_append_column(tree2, column)
	k.gtk_box_append(box,tree2)

def show(h):
	s = h.status()
	if h.is_seed():
		val=gtk.c_int()
		gtk.gtk_tree_model_get(list,ip,COLUMNS.progress,gtk.byref(val))
		if val.value<100:
			gtk.gtk_list_store_set5(list, ip,
				COLUMNS.progress, 100,
				COLUMNS.download_rate, str(0).encode(),
				COLUMNS.upload_rate, str(s.upload_rate / 1000).encode(),
				COLUMNS.num_peers, str(s.num_peers).encode(),
				COLUMNS.state, torrent.state_str[s.state])
		else:
			gtk.gtk_list_store_set2(list, ip,
				COLUMNS.upload_rate, str(s.upload_rate / 1000).encode(),
				COLUMNS.num_peers, str(s.num_peers).encode())
	else:
		gtk.gtk_list_store_set5(list, ip,
			COLUMNS.progress, int(s.progress * 100),
			COLUMNS.download_rate, str(s.download_rate / 1000).encode(),
			COLUMNS.upload_rate, str(s.upload_rate / 1000).encode(),
			COLUMNS.num_peers, str(s.num_peers).encode(),
			COLUMNS.state, torrent.state_str[s.state])
	gtk.gtk_list_store_set5(list2, ip2,
		COLUMNS2.list_peers, str(s.list_peers).encode(),
		COLUMNS2.num_complete, str(s.num_complete).encode(),
		COLUMNS2.num_incomplete, str(s.num_incomplete).encode(),
		COLUMNS2.next_announce, str(s.next_announce).encode(),
		COLUMNS2.last_upload, str(s.last_upload).encode())
