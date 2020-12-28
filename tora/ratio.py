try:
	import gtk
except Exception:
	from . import gtk
k=gtk.k

def text(a):
	tx=k.gtk_label_new(a)
	k.gtk_widget_set_halign(tx,gtk.GtkAlign.GTK_ALIGN_START)
	return tx
def edit():
	e=k.gtk_entry_new()
	k.gtk_widget_set_hexpand(e,True)
	return e

def ini():
	grid = k.gtk_grid_new ()
	k.gtk_grid_attach(grid,text(b"Interval time to verify in minutes (0=disable)"),0,0,1,1)
	ratint=edit()
	k.gtk_grid_attach(grid,ratint,1,0,1,1)
	k.gtk_grid_attach(grid,text(b"Value"),0,1,1,1)
	ratlim=edit()
	k.gtk_grid_attach(grid,ratlim,1,1,1,1)
	#
	fr=k.gtk_frame_new(b"Close program when Ratio is greater than Value and all torrents are seeds")
	k.gtk_frame_set_child(fr,grid)
	return fr