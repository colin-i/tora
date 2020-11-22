
from enum import IntEnum
class GConnectFlags(IntEnum):
	G_CONNECT_SWAPPED = 1 << 1
class GtkOrientation(IntEnum):
	GTK_ORIENTATION_HORIZONTAL=0
	GTK_ORIENTATION_VERTICAL=1
class GtkSortType(IntEnum):
	GTK_SORT_ASCENDING=0

#define G_TYPE_FUNDAMENTAL_SHIFT (2)
#define G_TYPE_MAKE_FUNDAMENTAL(x) ((GType) ((x) << G_TYPE_FUNDAMENTAL_SHIFT))
#define G_TYPE_STRING G_TYPE_MAKE_FUNDAMENTAL (16)
G_TYPE_STRING=0x40

import os
from ctypes import *

CALLBACK = CFUNCTYPE(c_void_p,c_void_p)

class GtkTreeIter(Structure):
    _fields_=[("stamp",c_int),("user_data",c_void_p),("user2_data",c_void_p),("user_data3",c_void_p)]

path_to_deps = "/usr/local/lib/arm-linux-gnueabihf"
os.environ['PATH'] = path_to_deps + os.pathsep + os.environ['PATH']
k = cdll.LoadLibrary("libgtk-4.so")#.0.9902.0")
#default is c_long (32/64,only 32 windows),argtypes may follow
ptr=c_void_p
int=c_int

k.g_application_run.argtypes = [ptr,int,ptr]
k.g_object_unref.argtypes = [ptr]
k.g_signal_connect_data.argtypes = [ptr,ptr,ptr,ptr,ptr,int]
#A
k.gtk_application_new.restype=ptr
k.gtk_application_new.argtypes=[ptr,int]
k.gtk_application_window_new.restype=ptr
k.gtk_application_window_new.argtypes = [ptr]
#B
k.gtk_box_append.argtypes = [ptr,ptr]
k.gtk_box_new.restype=ptr
k.gtk_box_new.argtypes = [int,int]
k.gtk_button_new_with_label.restype=ptr
k.gtk_button_new_with_label.argtypes = [ptr]
#C
k.gtk_cell_renderer_text_new.restype=ptr
#E
k.gtk_entry_buffer_get_text.restype=ptr
k.gtk_entry_buffer_get_text.argtypes = [ptr]
k.gtk_entry_get_buffer.restype=ptr
k.gtk_entry_get_buffer.argtypes = [ptr]
k.gtk_entry_new.restype=ptr
#L
k.gtk_list_store_new.restype=ptr
k.gtk_list_store_new.argtypes = [int,int,int]
#S
k.gtk_scrolled_window_new.restype=ptr
k.gtk_scrolled_window_set_child.argtypes = [ptr,ptr]
#T
k.gtk_tree_model_sort_new_with_model.restype=ptr
k.gtk_tree_model_sort_new_with_model.argtypes = [ptr]
k.gtk_tree_sortable_set_sort_column_id.restype=ptr
k.gtk_tree_sortable_set_sort_column_id.argtypes=[ptr,int,int]
k.gtk_tree_view_append_column.argtypes = [ptr,ptr]
k.gtk_tree_view_column_new_with_attributes.restype=ptr
k.gtk_tree_view_column_new_with_attributes.argtypes = [ptr,ptr,ptr,int,ptr]
k.gtk_tree_view_new_with_model.restype=ptr
k.gtk_tree_view_new_with_model.argtypes = [ptr]
k.gtk_tree_view_set_headers_visible.argtypes = [ptr,int]
#W
k.gtk_widget_show.argtypes=[ptr]
k.gtk_window_set_child.argtypes = [ptr,ptr]
k.gtk_window_set_title.argtypes=[ptr,ptr]