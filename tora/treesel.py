try:
	import gtk
	import layout
except Exception:
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
	f(item_text,data)
	k.g_free(item_text)
