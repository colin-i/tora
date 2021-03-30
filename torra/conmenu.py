from . import gtk
from . import meninfo
from . import torrent
from . import treesel
from . import layout
from . import next
k=gtk.k

timer=0

@gtk.CALLBACK0i
def fire():
	global timer
	k.gtk_widget_hide(menu)
	timer=0
	return False

@gtk.CALLBACK2
def click(tree,path):
	global timer
	if timer>0:
		k.g_source_remove(timer)
	k.gtk_widget_show(menu)
	torrent.sel(tree,path)
	timer=k.g_timeout_add(10000,fire,None)

def hide():
	global timer
	k.g_source_remove(timer)
	timer=0
	k.gtk_widget_hide(menu)

def remtor(i,iter):
	torrent.remsel(i)
	k.gtk_list_store_remove(layout.list,iter)
@gtk.CALLBACK
def remclick(tree):
	treesel.position__iter(remtor,tree)
	if k.gtk_tree_model_iter_n_children(layout.list,None)==0:
		next.unini(tree)
	hide()

@gtk.CALLBACK2
def infoclick(b,t):
	meninfo.act(b,t)
	hide()

def ini(parent,tree):
	global menu
	menu=k.gtk_box_new(gtk.GtkOrientation.GTK_ORIENTATION_HORIZONTAL,0)
	uni=chr(0x24D8).encode()
	b=k.gtk_button_new_with_label(uni)
	k.g_signal_connect_data(b,b"clicked",infoclick,tree,None,0)
	k.gtk_box_append(menu,b)
	uni=chr(0x1F5D1).encode()
	b=k.gtk_button_new_with_label(uni)
	k.g_signal_connect_data(b,b"clicked",remclick,tree,None,gtk.GConnectFlags.G_CONNECT_SWAPPED)
	k.gtk_box_append(menu,b)
	k.gtk_box_append(parent,menu)
	k.gtk_widget_hide(menu)
	k.g_signal_connect_data(tree,b"row-activated",click,None,None,0)
	k.gtk_tree_view_set_activate_on_single_click(tree,True)
