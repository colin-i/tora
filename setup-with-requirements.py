
reqs='python-libtorrent>=2.0.2'
from os import uname
if uname().machine!='armv7l':
	reqs='python-libtorrent-bin>=2.0.2'

import subprocess
import sys
test=subprocess.run([sys.executable,'-m','pip','install',reqs])
if test.returncode:
	exit(test.returncode)
import libtorrent
print('libtorrent found')

from ctypes import cdll
cdll.LoadLibrary("libgtk-4.so")
print('gtk4 found')

subprocess.run([sys.executable,'-m','pip','install','--user','.'])
