
"""
comment
"""

import os
import ctypes
#from ctypes import *

CALLBACK = ctypes.CFUNCTYPE(ctypes.c_void_p,ctypes.c_void_p)

@CALLBACK
def activate(app):
	window = k.gtk_application_window_new (app);
	k.gtk_window_set_title (window, b"Torrent");
#	k.gtk_window_set_default_size (window, 200, 200);
	k.gtk_widget_show (window)

def main():
	#k.g_signal_connect_data.argtypes = [ctypes.c_void_p,ctypes.c_void_p,ctypes.c_void_p,ctypes.c_void_p,ctypes.c_void_p,ctypes.c_int]
	#The problem is that, by default, ctypes assumes that all functions return int, which is 32 bits.
	k.gtk_application_new.restype=ctypes.c_void_p
	k.gtk_application_window_new.restype=ctypes.c_void_p	
	a=k.gtk_application_new(None,None)
	k.g_signal_connect_data (a, b"activate", activate, None, None, 0)
	r=k.g_application_run (a,None,None)
	k.g_object_unref(a)
	exit(r)

path_to_deps = "/usr/local/lib/arm-linux-gnueabihf"
os.environ['PATH'] = path_to_deps + os.pathsep + os.environ['PATH']
k = ctypes.cdll.LoadLibrary("libgtk-4.so")#.0.9902.0")

if __name__ == "__main__":
    main()
