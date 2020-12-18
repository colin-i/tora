
from enum import IntEnum
class GConnectFlags(IntEnum):
	G_CONNECT_SWAPPED = 1 << 1
class GtkDialogFlags(IntEnum):
	GTK_DIALOG_MODAL = 1 << 0
	GTK_DIALOG_DESTROY_WITH_PARENT = 1 << 1
class GtkOrientation(IntEnum):
	GTK_ORIENTATION_HORIZONTAL=0
	GTK_ORIENTATION_VERTICAL=1
class GtkResponseType(IntEnum):
	GTK_RESPONSE_NONE = -1
class GtkSortType(IntEnum):
	GTK_SORT_ASCENDING=0

#define G_TYPE_FUNDAMENTAL_SHIFT (2)
#define G_TYPE_MAKE_FUNDAMENTAL(x) ((GType) ((x) << G_TYPE_FUNDAMENTAL_SHIFT))
#define G_TYPE_STRING G_TYPE_MAKE_FUNDAMENTAL (16)
G_TYPE_STRING=0x40

import os
from ctypes import *

CALLBACK0b = CFUNCTYPE(c_bool)
CALLBACK0 = CFUNCTYPE(c_void_p)
CALLBACK = CFUNCTYPE(c_void_p,c_void_p)
CALLBACK3b = CFUNCTYPE(c_bool,c_void_p,c_void_p,c_void_p)

class GtkTreeIter(Structure):
    _fields_=[("stamp",c_int),("user_data",c_void_p),("user2_data",c_void_p),("user_data3",c_void_p)]

path_to_deps = "/usr/local/lib/arm-linux-gnueabihf"
os.environ['PATH'] = path_to_deps + os.pathsep + os.environ['PATH']
k = cdll.LoadLibrary("libgtk-4.so")#.0.9905.0")
#restype default is C int
#argtypes no default. c_void_p is python int. pointers must be announced
#two different variadic must be treated with casts, or use valist versions

k.g_application_run.argtypes = [c_void_p,c_int,c_void_p]
k.g_free.argtypes = [c_void_p]
k.g_object_unref.argtypes = [c_void_p]
k.g_signal_connect_data.argtypes = [c_void_p,c_void_p,c_void_p,c_void_p,c_void_p,c_int]
k.g_timeout_add.argtypes=[c_int,c_void_p]
#A
k.gtk_application_new.restype=c_void_p
k.gtk_application_new.argtypes=[c_void_p,c_int]
k.gtk_application_window_new.restype=c_void_p
k.gtk_application_window_new.argtypes = [c_void_p]
#B
k.gtk_box_append.argtypes = [c_void_p,c_void_p]
k.gtk_box_new.restype=c_void_p
k.gtk_button_new_with_label.restype=c_void_p
k.gtk_button_new_with_label.argtypes = [c_void_p]
#C
k.gtk_cell_renderer_text_new.restype=c_void_p
#D
k.gtk_dialog_get_content_area.restype=c_void_p
k.gtk_dialog_get_content_area.argtypes = [c_void_p]
k.gtk_dialog_new_with_buttons.restype=c_void_p
k.gtk_dialog_new_with_buttons.argtypes = [c_void_p,c_void_p,c_int,c_void_p,c_int,c_void_p]
#E
k.gtk_entry_buffer_get_text.restype=c_char_p
k.gtk_entry_buffer_get_text.argtypes = [c_void_p]
k.gtk_entry_buffer_new.restype=c_void_p
k.gtk_entry_get_buffer.restype=c_void_p
k.gtk_entry_get_buffer.argtypes = [c_void_p]
k.gtk_entry_new.restype=c_void_p
k.gtk_entry_new_with_buffer.restype=c_void_p
k.gtk_entry_new_with_buffer.argtypes = [c_void_p]
#L
k.gtk_label_new.restype=c_void_p
k.gtk_label_new.argtypes = [c_void_p]
k.gtk_list_store_new.restype=c_void_p
k.gtk_list_store_set.argtypes = [c_void_p,c_void_p,c_int,c_void_p,c_int,c_void_p,c_int]
#S
k.gtk_scrolled_window_new.restype=c_void_p
k.gtk_scrolled_window_set_child.argtypes = [c_void_p,c_void_p]
#T
k.gtk_tree_model_foreach.argtypes = [c_void_p,c_void_p]
k.gtk_tree_model_get.argtypes = [c_void_p,c_void_p,c_int,POINTER(c_char_p),c_int,POINTER(c_char_p),c_int]
k.gtk_tree_model_sort_new_with_model.restype=c_void_p
k.gtk_tree_model_sort_new_with_model.argtypes = [c_void_p]
k.gtk_tree_sortable_set_sort_column_id.argtypes=[c_void_p,c_int,c_int]
k.gtk_tree_view_append_column.argtypes = [c_void_p,c_void_p]
k.gtk_tree_view_column_new_with_attributes.restype=c_void_p
k.gtk_tree_view_column_new_with_attributes.argtypes = [c_void_p,c_void_p,c_void_p,c_int,c_void_p]
k.gtk_tree_view_new_with_model.restype=c_void_p
k.gtk_tree_view_new_with_model.argtypes = [c_void_p]
k.gtk_tree_view_set_activate_on_single_click.argtypes = [c_void_p,c_int]
k.gtk_tree_view_set_headers_visible.argtypes = [c_void_p,c_int]
#W
k.gtk_widget_hide.argtypes=[c_void_p]
k.gtk_widget_set_hexpand.argtypes=[c_void_p,c_int]
k.gtk_widget_set_vexpand.argtypes=[c_void_p,c_int]
k.gtk_widget_show.argtypes=[c_void_p]
k.gtk_window_get_default_size.argtypes=[c_void_p,c_void_p,c_void_p]
k.gtk_window_is_maximized.argtypes=[c_void_p]
k.gtk_window_maximize.argtypes=[c_void_p]
k.gtk_window_set_child.argtypes = [c_void_p,c_void_p]
k.gtk_window_set_default_size.argtypes=[c_void_p,c_int,c_int]
k.gtk_window_set_title.argtypes=[c_void_p,c_void_p]