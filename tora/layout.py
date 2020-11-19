import gtk
k=gtk.k
def layout(window):
	bx=k.gtk_box_new(gtk.GtkOrientation.GTK_ORIENTATION_HORIZONTAL,0)
	e=k.gtk_entry_new()
	b=k.gtk_button_new_with_label(b"+")
	#
	k.gtk_box_append(bx,e)
	k.gtk_box_append(bx,b)
	#
	box=k.gtk_box_new(gtk.GtkOrientation.GTK_ORIENTATION_VERTICAL,0)
	scroll = k.gtk_scrolled_window_new ()
	k.gtk_box_append(box,bx)
	k.gtk_box_append(box,scroll)
	k.gtk_window_set_child(window,box)
