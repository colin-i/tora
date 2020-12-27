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
	f(item_text.value.decode(),data)
	k.g_free(item_text)

def position(f,tree):
	mod=gtk.c_void_p()
	it=gtk.GtkTreeIter()
	i=gtk.byref(it)
	sl=k.gtk_tree_view_get_selection(tree)
	k.gtk_tree_selection_get_selected(sl,gtk.byref(mod),i)
	p=gtk.c_int()
	gtk.gtk_tree_model_get(mod,i,layout.COLUMNS.INDEX,gtk.byref(p))
	f(p.value)

def position__iter(f,tree):
	mod=gtk.c_void_p()
	it=gtk.GtkTreeIter()
	i=gtk.byref(it)
	sl=k.gtk_tree_view_get_selection(tree)
	k.gtk_tree_selection_get_selected(sl,gtk.byref(mod),i)
	p=gtk.c_int()
	gtk.gtk_tree_model_get(mod,i,layout.COLUMNS.INDEX,gtk.byref(p))
	it2=gtk.GtkTreeIter()
	i2=gtk.byref(it2)
	k.gtk_tree_model_sort_convert_iter_to_child_iter(mod,i2,i)
	f(p.value,i2)
