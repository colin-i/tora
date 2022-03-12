
import subprocess
import sys

try:
   import libtorrent
except Exception:
	test=subprocess.run([sys.executable,'-m','pip','install','python-libtorrent-bin>=1.2.9'])
	if test.returncode:
		subprocess.run([sys.executable,'-m','pip','install','python-libtorrent>=1.2.9'])
		if test.returncode:
			exit(test.returncode)
		import libtorrent
print('libtorrent found')

from ctypes import cdll
cdll.LoadLibrary("libgtk-4.so")
print('gtk4 found')

subprocess.run([sys.executable,'-m','pip','install','--user','.'])
