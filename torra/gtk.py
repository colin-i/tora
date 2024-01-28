
from enum import IntEnum,auto
class GdkModifierType(IntEnum):
	GDK_CONTROL_MASK = 1 << 2
	GDK_ALT_MASK = 1 << 3
class GdkToplevelState(IntEnum):
	GDK_TOPLEVEL_STATE_MINIMIZED = 1 << 0
class GtkAlign(IntEnum):
	GTK_ALIGN_START = auto()
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
	GTK_SORT_DESCENDING=1
class GtkWrapMode(IntEnum):
	GTK_WRAP_WORD_CHAR=3

G_TYPE_FUNDAMENTAL_SHIFT = 2
G_TYPE_MAKE_FUNDAMENTAL=lambda x: x << G_TYPE_FUNDAMENTAL_SHIFT
G_TYPE_STRING=G_TYPE_MAKE_FUNDAMENTAL (16)
G_TYPE_INT=G_TYPE_MAKE_FUNDAMENTAL (6)
GDK_KEY_n=0x06e

import os
from ctypes import *

CALLBACK0i = CFUNCTYPE(c_int)
CALLBACK = CFUNCTYPE(None,c_void_p)
CALLBACKi = CFUNCTYPE(c_int,c_void_p)
CALLBACK2 = CFUNCTYPE(None,c_void_p,c_void_p)
CALLBACK3 = CFUNCTYPE(None,c_void_p,c_int,c_void_p)
CALLBACK4i = CFUNCTYPE(c_int,c_void_p,c_int,c_int,c_int)

class GtkTreeIter(Structure):
	_fields_=[("stamp",c_int),("user_data",c_void_p),("user_data2",c_void_p),("user_data3",c_void_p)]

path_to_deps = "/usr/local/lib/arm-linux-gnueabihf"
os.environ['PATH'] = path_to_deps + os.pathsep + os.environ['PATH']
lib_gtk_name="libgtk-4.so.1"
k = cdll.LoadLibrary(lib_gtk_name)

#By default functions are assumed to return the C int type. Other return types can be specified by setting the restype attribute of the function object.
#argtypes no default. c_void_p is python int. pointers must be announced on ARM.
#variadics are troubles

def gtk_tree_model_get(a,b,i1,p1):
	k.gtk_tree_model_get.argtypes=[c_void_p,c_void_p,c_int,c_void_p,c_int]
	k.gtk_tree_model_get(a,b,i1,p1,-1)
def gtk_tree_model_get2(a,b,i1,p1,i2,p2):
	k.gtk_tree_model_get.argtypes=[c_void_p,c_void_p,c_int,c_void_p,c_int,c_void_p,c_int]
	k.gtk_tree_model_get(a,b,i1,p1,i2,p2,-1)
def gtk_list_store_set2(a,b,i1,p1,i2,p2):
	k.gtk_list_store_set.argtypes = [c_void_p,c_void_p,c_int,c_void_p,c_int,c_void_p,c_int]
	k.gtk_list_store_set(a,b,i1,p1,i2,p2,-1)
def gtk_list_store_set3(a,b,i1,p1,i2,p2,i3,p3):
	k.gtk_list_store_set.argtypes = [c_void_p,c_void_p,c_int,c_void_p,c_int,c_void_p,c_int,c_void_p,c_int]
	k.gtk_list_store_set(a,b,i1,p1,i2,p2,i3,p3,-1)
def gtk_list_store_set5(a,b,i1,v1,i2,p2,i3,p3,i4,p4,i5,p5):
	k.gtk_list_store_set.argtypes = [c_void_p,c_void_p,c_int,c_void_p,c_int,c_void_p,c_int,c_void_p,c_int,c_void_p,c_int,c_void_p,c_int]
	k.gtk_list_store_set(a,b,i1,v1,i2,p2,i3,p3,i4,p4,i5,p5,-1)

k.g_application_run.argtypes = [c_void_p,c_int,c_void_p]
k.g_free.argtypes = [c_void_p]
k.g_object_unref.argtypes = [c_void_p]
k.g_signal_connect_data.argtypes = [c_void_p,c_void_p,c_void_p,c_void_p,c_void_p,c_int]
k.g_source_remove.argtypes = [c_void_p]
k.g_timeout_add.argtypes = [c_int,c_void_p,c_void_p]
#
k.gdk_keyval_name.restype=c_char_p
k.gdk_toplevel_get_state.argtypes = [c_void_p]
#A
k.gtk_application_new.restype=c_void_p
k.gtk_application_new.argtypes=[c_void_p,c_int]
k.gtk_application_window_new.restype=c_void_p
k.gtk_application_window_new.argtypes = [c_void_p]
#BO
k.gtk_box_append.argtypes = [c_void_p,c_void_p]
k.gtk_box_new.restype=c_void_p
#BU
k.gtk_button_new_with_label.restype=c_void_p
k.gtk_button_new_with_label.argtypes = [c_void_p]
#C
k.gtk_cell_renderer_progress_new.restype=c_void_p
k.gtk_cell_renderer_text_new.restype=c_void_p
#D
k.gtk_dialog_get_content_area.restype=c_void_p
k.gtk_dialog_get_content_area.argtypes = [c_void_p]
k.gtk_dialog_new_with_buttons.restype=c_void_p
k.gtk_dialog_new_with_buttons.argtypes = [c_void_p,c_void_p,c_int,c_void_p,c_int,c_void_p]
#EN
k.gtk_entry_buffer_get_text.restype=c_char_p
k.gtk_entry_buffer_get_text.argtypes = [c_void_p]
k.gtk_entry_buffer_new.restype=c_void_p
k.gtk_entry_buffer_set_text.argtypes = [c_void_p,c_void_p,c_int]
k.gtk_entry_get_buffer.restype=c_void_p
k.gtk_entry_get_buffer.argtypes = [c_void_p]
k.gtk_entry_new.restype=c_void_p
k.gtk_entry_new_with_buffer.restype=c_void_p
k.gtk_entry_new_with_buffer.argtypes = [c_void_p]
#EV
k.gtk_event_controller_key_new.restype=c_void_p
#F
k.gtk_frame_new.restype=c_void_p
k.gtk_frame_new.argtypes = [c_void_p]
k.gtk_frame_set_child.argtypes = [c_void_p,c_void_p]
#G
k.gtk_grid_attach.argtypes = [c_void_p,c_void_p,c_int,c_int,c_int,c_int]
k.gtk_grid_new.restype=c_void_p
#LA
k.gtk_label_new.restype=c_void_p
k.gtk_label_new.argtypes = [c_void_p]
#LI
k.gtk_list_store_append.argtypes = [c_void_p,c_void_p]
k.gtk_list_store_new.restype=c_void_p
k.gtk_list_store_prepend.argtypes = [c_void_p,c_void_p]
k.gtk_list_store_remove.argtypes = [c_void_p,c_void_p]
#N
k.gtk_native_get_surface.restype=c_void_p
k.gtk_native_get_surface.argtypes = [c_void_p]
#SC
k.gtk_scrolled_window_new.restype=c_void_p
k.gtk_scrolled_window_set_child.argtypes = [c_void_p,c_void_p]
#TEB
k.gtk_text_buffer_set_text.argtypes = [c_void_p,c_void_p,c_int]
#TEV
k.gtk_text_view_get_buffer.restype=c_void_p
k.gtk_text_view_get_buffer.argtypes = [c_void_p]
k.gtk_text_view_new.restype=c_void_p
k.gtk_text_view_set_editable.argtypes=[c_void_p,c_int]
k.gtk_text_view_set_wrap_mode.argtypes=[c_void_p,c_int]
#TEW
k.gtk_test_widget_wait_for_draw.argtypes = [c_void_p]
#TM
k.gtk_tree_model_get_iter_first.argtypes = [c_void_p,c_void_p]
k.gtk_tree_model_get_path.restype=c_void_p
k.gtk_tree_model_get_path.argtypes = [c_void_p,c_void_p]
k.gtk_tree_model_iter_n_children.argtypes = [c_void_p,c_void_p]
k.gtk_tree_model_iter_next.argtypes = [c_void_p,c_void_p]
k.gtk_tree_model_sort_convert_iter_to_child_iter.argtypes = [c_void_p,c_void_p,c_void_p]
k.gtk_tree_model_sort_convert_path_to_child_path.restype=c_void_p
k.gtk_tree_model_sort_convert_path_to_child_path.argtypes = [c_void_p,c_void_p]
k.gtk_tree_model_sort_new_with_model.restype=c_void_p
k.gtk_tree_model_sort_new_with_model.argtypes = [c_void_p]
#TP
k.gtk_tree_path_free.argtypes = [c_void_p]
k.gtk_tree_path_get_indices.restype=POINTER(c_int)
k.gtk_tree_path_get_indices.argtypes = [c_void_p]
#TS
k.gtk_tree_selection_get_selected.argtypes = [c_void_p,c_void_p,c_void_p]
k.gtk_tree_selection_select_path.argtypes = [c_void_p,c_void_p]
k.gtk_tree_sortable_get_sort_column_id.argtypes=[c_void_p,c_void_p,c_void_p]
k.gtk_tree_sortable_set_sort_column_id.argtypes=[c_void_p,c_int,c_int]
#TV
k.gtk_tree_view_get_selection.restype=c_void_p
k.gtk_tree_view_get_selection.argtypes = [c_void_p]
k.gtk_tree_view_append_column.argtypes = [c_void_p,c_void_p]
#TVC
k.gtk_tree_view_column_new_with_attributes.restype=c_void_p
k.gtk_tree_view_column_new_with_attributes.argtypes = [c_void_p,c_void_p,c_void_p,c_int,c_void_p]
k.gtk_tree_view_column_set_clickable.argtypes=[c_void_p,c_int]
k.gtk_tree_view_column_set_expand.argtypes=[c_void_p,c_int]
k.gtk_tree_view_column_set_resizable.argtypes = [c_void_p,c_int]
#
k.gtk_tree_view_new_with_model.restype=c_void_p
k.gtk_tree_view_new_with_model.argtypes = [c_void_p]
k.gtk_tree_view_set_activate_on_single_click.argtypes = [c_void_p,c_int]
#WID
k.gtk_widget_add_controller.argtypes = [c_void_p,c_void_p]
k.gtk_widget_get_height.argtypes=[c_void_p]
k.gtk_widget_get_root.restype=c_void_p
k.gtk_widget_get_root.argtypes=[c_void_p]
k.gtk_widget_get_width.argtypes=[c_void_p]
k.gtk_widget_hide.argtypes=[c_void_p]
k.gtk_widget_remove_controller.argtypes = [c_void_p,c_void_p]
k.gtk_widget_set_halign.argtypes = [c_void_p,c_int]
k.gtk_widget_set_hexpand.argtypes=[c_void_p,c_int]
k.gtk_widget_set_vexpand.argtypes=[c_void_p,c_int]
k.gtk_widget_show.argtypes=[c_void_p]
#WIN
k.gtk_window_close.argtypes=[c_void_p]
k.gtk_window_destroy.argtypes=[c_void_p]
k.gtk_window_get_default_size.argtypes=[c_void_p,c_void_p,c_void_p]
k.gtk_window_is_maximized.argtypes=[c_void_p]
k.gtk_window_maximize.argtypes=[c_void_p]
k.gtk_window_minimize.argtypes=[c_void_p]
k.gtk_window_set_child.argtypes = [c_void_p,c_void_p]
k.gtk_window_set_default_size.argtypes=[c_void_p,c_int,c_int]
k.gtk_window_set_title.argtypes=[c_void_p,c_void_p]
