
try:
	import gtk
	import ratio
except Exception:
	from . import gtk
	from . import ratio
k=gtk.k

fold_bf=k.gtk_entry_buffer_new(None,-1)

@gtk.CALLBACK
def sets(window):
	dialog = k.gtk_dialog_new_with_buttons (b"Settings",window,
		gtk.GtkDialogFlags.GTK_DIALOG_DESTROY_WITH_PARENT | gtk.GtkDialogFlags.GTK_DIALOG_MODAL,
		b"_OK",gtk.GtkResponseType.GTK_RESPONSE_NONE,None)
	width=gtk.c_int()
	height=gtk.c_int()
	k.gtk_window_get_default_size (window, gtk.byref(width), gtk.byref(height))
	k.gtk_window_set_default_size(dialog,width,height)
	k.g_signal_connect_data (dialog,b"response",k.gtk_window_destroy,None,None,0)
	#
	box=k.gtk_dialog_get_content_area(dialog)
	k.gtk_orientable_set_orientation(box,gtk.GtkOrientation.GTK_ORIENTATION_VERTICAL)
	#
	t=k.gtk_label_new (b"Download Folder")
	e=k.gtk_entry_new_with_buffer(fold_bf)
	k.gtk_widget_set_hexpand(e,True)
	bx=k.gtk_box_new(gtk.GtkOrientation.GTK_ORIENTATION_HORIZONTAL,0)
	k.gtk_box_append(bx, t)
	k.gtk_box_append(bx, e)
	#
	k.gtk_box_append(box, bx)
	k.gtk_box_append(box, ratio.ini())
	#
	k.gtk_widget_show (dialog)
