from . import gtk
from . import treesel
from . import bencod
k=gtk.k

def go(path,window):
	with open(path,'rb') as f:
		d=f.read()
		bencod.is_info=True
		a=bencod.decode(d)
		bencod.is_info=False
		dialog = k.gtk_dialog_new_with_buttons (b"Info",window,
			gtk.GtkDialogFlags.GTK_DIALOG_DESTROY_WITH_PARENT | gtk.GtkDialogFlags.GTK_DIALOG_MODAL,
			b"_OK",gtk.GtkResponseType.GTK_RESPONSE_NONE,None)

		#same like settings
		k.gtk_window_set_default_size(dialog,k.gtk_widget_get_width(window),k.gtk_widget_get_height(window))

		k.g_signal_connect_data (dialog,b"response",k.gtk_window_destroy,None,None,0)
		box=k.gtk_dialog_get_content_area(dialog)
		#
		text = k.gtk_text_view_new ()
		k.gtk_text_view_set_editable(text, False)
		k.gtk_text_view_set_wrap_mode(text,gtk.GtkWrapMode.GTK_WRAP_WORD_CHAR)
		text_buffer = k.gtk_text_view_get_buffer (text)
		k.gtk_text_buffer_set_text (text_buffer,str(a).encode(),-1)
		#
		scrolled_window = k.gtk_scrolled_window_new ()
		k.gtk_scrolled_window_set_child (scrolled_window,text)
		k.gtk_box_append(box, scrolled_window)
		k.gtk_widget_set_hexpand(scrolled_window,True)
		k.gtk_widget_set_vexpand(scrolled_window,True)
		#
		k.gtk_widget_show (dialog)

def act(button,tree):
	treesel.text(go,tree,k.gtk_widget_get_root(button))
