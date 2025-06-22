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
		if sys.argv[1]=="--debug":
			sys.stdout.write("ENTRY_DEBUG marker\n")
			sys.stdout.flush()
		else:
			fname=sys.argv[1]
			if len(fname)==1:
				if len(sys.argv)>2:
					if fname[0]=='f':
						fname=sys.argv[2]
			listtor.config_filename=fname
	os.makedirs(confs.get_root_dir(),exist_ok=True)
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
		print("Would remove(dirs only if empty):")
		f1=cleanup_f(confs.configs_filename)
		f2=cleanup_f(listtor.config_filename)
		print(c)
		base=os.path.dirname(c)
		if (os.path.basename(base))[0]=='.': #.config, on another system can be a premade
			print(base)
		else:
			base=None
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
				if base:
					if len(os.listdir(path=base))==0:
						os.rmdir(base)
						print(base.__str__()+r)
					else:
						print(base.__str__()+" is not empty.")
			else:
				print(c.__str__()+" is not empty.")
		else:
			print("expecting \"yes\"")

if __name__ == "__main__":
	main()
