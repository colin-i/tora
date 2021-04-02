#setuptools.setup is looking at one argv parameter; to "build" and "install":
#python3 setup.py install

pkname='torra'

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
from ctypes import cdll
cdll.LoadLibrary("libgtk-4.so")

import pathlib
HERE = pathlib.Path(__file__).parent
README = (HERE / "README.md").read_text()

from setuptools import setup
setup(name=pkname,
	version='1.0.1',
	packages=[pkname],
	install_requires=[reqs],#still lazy for bdist_wheel
	description='Torrent client',
	long_description=README,
	long_description_content_type="text/markdown",
	url='https://github.com/colin-i/tora',
	author='bot',
	author_email='costin.botescu@gmail.com',
	license='MIT',
	zip_safe=False,
	entry_points = {
		'console_scripts': [pkname+'='+pkname+'.main:main']
	}
)
