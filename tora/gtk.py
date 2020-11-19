from enum import IntEnum
class GtkOrientation(IntEnum):
	GTK_ORIENTATION_HORIZONTAL=0
	GTK_ORIENTATION_VERTICAL=1

import os
import ctypes

path_to_deps = "/usr/local/lib/arm-linux-gnueabihf"
os.environ['PATH'] = path_to_deps + os.pathsep + os.environ['PATH']
k = ctypes.cdll.LoadLibrary("libgtk-4.so")#.0.9902.0")
#default is c_long (32/64,only 32 windows),argtypes may follow
ptr=ctypes.c_void_p
int=ctypes.c_int

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
#E
k.gtk_entry_new.restype=ptr
#S
k.gtk_scrolled_window_new.restype=ptr
#W
k.gtk_widget_show.argtypes=[ptr]
k.gtk_window_set_child.argtypes = [ptr,ptr]
k.gtk_window_set_title.argtypes=[ptr,ptr]
