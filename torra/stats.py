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

list=k.gtk_list_store_new(COLUMNS.N, gtk.G_TYPE_INT, gtk.G_TYPE_STRING, gtk.G_TYPE_STRING, gtk.G_TYPE_STRING, gtk.G_TYPE_STRING)
i=gtk.GtkTreeIter()
ip=gtk.byref(i)
k.gtk_list_store_append(list,ip)

def ini(box):
	tree=k.gtk_tree_view_new_with_model(list)
	k.g_object_unref(list)
	renderer = k.gtk_cell_renderer_progress_new()
	column = k.gtk_tree_view_column_new_with_attributes(b"Percentage", renderer, b"value", COLUMNS.progress, None)
	k.gtk_tree_view_append_column(tree, column)
	renderer = k.gtk_cell_renderer_text_new()
	column = k.gtk_tree_view_column_new_with_attributes(b"Download kB/s", renderer, b"text", COLUMNS.download_rate, None)
	k.gtk_tree_view_append_column(tree, column)
	renderer = k.gtk_cell_renderer_text_new()
	column = k.gtk_tree_view_column_new_with_attributes(b"Upload kB/s", renderer, b"text", COLUMNS.upload_rate, None)
	k.gtk_tree_view_append_column(tree, column)
	renderer = k.gtk_cell_renderer_text_new()
	column = k.gtk_tree_view_column_new_with_attributes(b"Peers num", renderer, b"text", COLUMNS.num_peers, None)
	k.gtk_tree_view_append_column(tree, column)
	renderer = k.gtk_cell_renderer_text_new()
	column = k.gtk_tree_view_column_new_with_attributes(b"State", renderer, b"text", COLUMNS.state, None)
	k.gtk_tree_view_append_column(tree, column)
	k.gtk_box_append(box,tree)

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
