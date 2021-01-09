
try:
	import gtk
	import ratio
	import next
	import log
except Exception:
	from . import gtk
	from . import ratio
	from . import next
	from . import log
k=gtk.k

fold_bf=k.gtk_entry_buffer_new(None,-1)

def labent(t,e):
	t=k.gtk_label_new (t)
	k.gtk_widget_set_hexpand(e,True)
	bx=k.gtk_box_new(gtk.GtkOrientation.GTK_ORIENTATION_HORIZONTAL,0)
	k.gtk_box_append(bx, t)
	k.gtk_box_append(bx, e)
	return bx

@gtk.CALLBACK3
def response(dialog,re,window):
	ratio.setint(window)
	k.gtk_window_destroy(dialog)

@gtk.CALLBACK
def sets(window):
	dialog = k.gtk_dialog_new_with_buttons (b"Settings",window,
		gtk.GtkDialogFlags.GTK_DIALOG_DESTROY_WITH_PARENT | gtk.GtkDialogFlags.GTK_DIALOG_MODAL,
		b"_OK",gtk.GtkResponseType.GTK_RESPONSE_NONE,None)
	width=gtk.c_int()
	height=gtk.c_int()
	k.gtk_window_get_default_size (window, gtk.byref(width), gtk.byref(height))
	k.gtk_window_set_default_size(dialog,width,height)
	k.g_signal_connect_data (dialog,b"response",response,window,None,0)
	#
	box=k.gtk_dialog_get_content_area(dialog)
	k.gtk_orientable_set_orientation(box,gtk.GtkOrientation.GTK_ORIENTATION_VERTICAL)
	#
	e=k.gtk_entry_new_with_buffer(fold_bf)
	k.gtk_box_append(box, labent(b"Download Folder",e))
	k.gtk_box_append(box, ratio.ini(window))
	e=k.gtk_entry_new()
	next.sets(e)
	k.gtk_box_append(box, labent(b"Go to the next unfinished torrent",e))
	k.gtk_box_append(box, labent(b"Log File",k.gtk_entry_new_with_buffer(log.log_bf)))
	#
	k.gtk_widget_show (dialog)
