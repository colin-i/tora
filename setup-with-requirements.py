
try:
   import libtorrent
except Exception:
	import subprocess
	import sys
	test=subprocess.run([sys.executable,'-m','pip','install','python-libtorrent-bin>=2.0.2'])
	if test.returncode:
		subprocess.run([sys.executable,'-m','pip','install','python-libtorrent>=2.0.2'])
		if test.returncode:
			exit(test.returncode)
		import libtorrent
print('libtorrent found')

from ctypes import cdll
cdll.LoadLibrary("libgtk-4.so")
print('gtk4 found')

subprocess.run([sys.executable,'-m','pip','install','--user','.'])
