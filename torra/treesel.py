from . import gtk
from . import layout
k=gtk.k

def text(f,tree,data):
	mod=gtk.c_void_p()
	it=gtk.GtkTreeIter()
	i=gtk.byref(it)
	sl=k.gtk_tree_view_get_selection(tree)
	k.gtk_tree_selection_get_selected(sl,gtk.byref(mod),i)
	item_text=gtk.c_char_p()
	gtk.gtk_tree_model_get (mod, i, layout.COLUMNS.PATH, gtk.byref(item_text))
	f(item_text.value,data)
	k.g_free(item_text)

def position__iter(f,tree):
	mod=gtk.c_void_p()
	it=gtk.GtkTreeIter()
	i=gtk.byref(it)
	sl=k.gtk_tree_view_get_selection(tree)
	k.gtk_tree_selection_get_selected(sl,gtk.byref(mod),i)
	path = k.gtk_tree_model_get_path (mod , i)
	p2=k.gtk_tree_model_sort_convert_path_to_child_path(mod,path)
	k.gtk_tree_path_free(path)
	ix=k.gtk_tree_path_get_indices ( p2 )
	ix=ix[0]
	k.gtk_tree_path_free(p2)
	#
	it2=gtk.GtkTreeIter()
	i2=gtk.byref(it2)
	k.gtk_tree_model_sort_convert_iter_to_child_iter(mod,i2,i)
	#
	f(ix,i2)
