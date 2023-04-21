from . import gtk
from . import torrent
from . import layout
k=gtk.k

mask=gtk.GdkModifierType.GDK_CONTROL_MASK
key=gtk.GDK_KEY_n

@gtk.CALLBACK4i
def eve(tree, keyval, keycode, state):
	if (state&mask)==mask:
		K=k.gdk_keyval_to_lower(keyval)#shiftlock+n is N and lock mod NOT n and mod
		if K==key:
			mod=gtk.c_void_p()
			it=gtk.GtkTreeIter()
			i=gtk.byref(it)
			sl=k.gtk_tree_view_get_selection(tree)
			k.gtk_tree_selection_get_selected(sl,gtk.byref(mod),i)
			p=k.gtk_tree_model_get_path(mod,i)
			ix=k.gtk_tree_path_get_indices ( p )
			ix=ix[0]
			k.gtk_tree_path_free(p)
			find(sl,mod,i,ix)
			return True
	return False

def ini(tree):
	global controller
	controller=k.gtk_event_controller_key_new()
	k.g_signal_connect_data (controller,b"key-pressed",eve,tree,None,gtk.GConnectFlags.G_CONNECT_SWAPPED)
	k.gtk_widget_add_controller (tree, controller)

def unini(tree):
	k.gtk_widget_remove_controller(tree,controller)
	
def find(sl,mod,it,pos):
	i2=gtk.GtkTreeIter()
	it2=gtk.byref(i2)
	b=k.gtk_tree_model_iter_next(mod,it)
	while b:
		if is_unfinished(mod,it,it2,sl):
			return
		b=k.gtk_tree_model_iter_next(mod,it)
	if pos>0:
		k.gtk_tree_model_get_iter_first(mod,it)
		while True:
			if is_unfinished(mod,it,it2,sl):
				return
			pos-=1
			if pos==0:
				break
			k.gtk_tree_model_iter_next(mod,it)

def is_unfinished(mod,it,it2,sl):
	k.gtk_tree_model_sort_convert_iter_to_child_iter(mod,it2,it)
	p2=k.gtk_tree_model_get_path(layout.list,it2)
	ix=k.gtk_tree_path_get_indices ( p2 )
	ix=ix[0]
	k.gtk_tree_path_free(p2)
	s=torrent.torrents[ix].h.status()
	if s.progress<1:
		p=k.gtk_tree_model_get_path(mod,it)
		k.gtk_tree_selection_select_path(sl,p)
		k.gtk_tree_path_free(p)
		torrent.pos(ix)
		return True
	return False

def sets(e):
	show(e)
	control=k.gtk_event_controller_key_new()
	k.g_signal_connect_data (control,b"key-pressed",reset,e,None,gtk.GConnectFlags.G_CONNECT_SWAPPED)
	k.gtk_widget_add_controller (e, control)

def show(e):
	if (mask&gtk.GdkModifierType.GDK_CONTROL_MASK)!=0:
		txt="Ctrl+"
	else:
		txt=""
	if (mask&gtk.GdkModifierType.GDK_ALT_MASK)!=0:
		txt+="Alt+"
	txt+=k.gdk_keyval_name(key).decode()
	bf=k.gtk_entry_get_buffer(e)
	k.gtk_entry_buffer_set_text(bf,txt.encode(),-1)

@gtk.CALLBACK4i
def reset(e, keyval, keycode, state):
	global mask,key
	mask=state&(gtk.GdkModifierType.GDK_CONTROL_MASK|gtk.GdkModifierType.GDK_ALT_MASK)
	key=keyval
	show(e)
	return True

def store(d):
	d['next_mask']=mask
	d['next_key']=key
def restore(d):
	global mask,key
	mask=d['next_mask']
	key=d['next_key']
