#setuptools.setup is looking at one argv parameter; to "build" and "install":
#python3 setup.py install

pkname='torra'

#cant put in egg info "libtorrent-bin or libtorrent", only one is
try:
   import libtorrent
except ImportError:
	import subprocess
	import sys
	test=subprocess.run([sys.executable,'-m','pip','install','python-libtorrent-bin>=2.0.2'])
	if test.returncode:
		subprocess.run([sys.executable,'-m','pip','install','python-libtorrent>=2.0.2'])

import pathlib
HERE = pathlib.Path(__file__).parent
README = (HERE / "README.md").read_text()

from setuptools import setup
setup(name=pkname,
	version='1.0.8',
	packages=[pkname],
	#opt
	python_requires='>=3',
	install_requires=["appdirs>=1.4.3"],
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
