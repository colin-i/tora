"""
torrent client
"""

import sys
import os

from . import confs
from . import gtk
from . import layout
from . import sets
from . import torrent
from . import overall
from . import listtor
from . import ratio
k=gtk.k

@gtk.CALLBACKi
def closing(window):
	listtor.write(layout.list)
	confs.write_opt(window)
	torrent.close()
	overall.close()
	ratio.freeint()
	return False

@gtk.CALLBACK
def activate(app):
	window = k.gtk_application_window_new (app)
	k.gtk_window_set_title (window, b"Torrent")
	k.g_signal_connect_data (window, b"close-request", closing, None, None, 0)
	k.gtk_widget_show (window)
	confs.read_opt(window)

	#wd=confs.width
	#if wd<0:
	#	confs.width=k.gtk_widget_get_width(window)
	#	if wd==-2:
	#		k.gtk_window_minimize(window)

	layout.layout(window)

def main():
	if len(sys.argv)>1:
		if sys.argv[1]=="--remove-config":
			cleanup()
			return
		listtor.config_filename=sys.argv[1].replace('\\','') #the same? pdb -m torra.main \\-\\-remove-config
	confs.get_root_dir().mkdir(exist_ok=True)
	a=k.gtk_application_new(None,0)
	actv=b"activate"
	k.g_signal_connect_data (a, actv, activate, None, None, 0)
	r=k.g_application_run (a,0,None)
	k.g_object_unref(sets.fold_bf)
	k.g_object_unref(a)
	exit(r)

def cleanup_f(f):
	if os.path.isfile(f):
		print(f)
		return f
	return None
def cleanup():
	c=confs.get_root_dir()
	if os.path.isdir(c):
		print("Would remove:")
		f1=cleanup_f(confs.configs_filename)
		f2=cleanup_f(listtor.config_filename)
		print(c)
		print("yes ?");
		str = ""
		while True:
			x = sys.stdin.read(1) # reads one byte at a time, similar to getchar()
			if x == '\n':
				break
			str += x
		if str=="yes":
			r=" removed"
			if f1:
				os.remove(f1)
				print(f1+r)
			if f2:
				os.remove(f2)
				print(f2+r)
			if len(os.listdir(path=c))==0:
				os.rmdir(c) #OSError if not empty
				print(c.__str__()+r)
			else:
				print(c.__str__()+" is not empty.")
		else:
			print("expecting \"yes\"")

if __name__ == "__main__":
	main()
