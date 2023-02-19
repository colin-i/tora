
#setuptools.setup is looking at one argv parameter; to "build" and "install":
#python3 setup.py install

#libtorrent from pypi has bindings and library now, before was:
#	python-libtorrent-bin is at extra require now, but, if was at install requires:
#		ok, package python-libtorrent-bin is old. install with pip install --no-deps but add somehow appdirs
#			and python-libtorrent on ubuntu
#			if it's not old python-libtorrent at pip:
#				that+(libtorrent-rasterbar2.0 on ubuntu) can be a solution

pkname='torra'

import pathlib
HERE = pathlib.Path(__file__).parent
#here README is ok, else will be README.md not found for pypi
README = (HERE / "info.md").read_text()
ver=(HERE / "v2").read_text()

from setuptools import setup
setup(name=pkname,
	version=ver,
	packages=[pkname],
	#opt
	python_requires='>=3',
	install_requires=["appdirs>=1.4.3"
		,"libtorrent"
		#python-libtorrent-bin it's not updated at pypi (old 3.9)
		#,'python-libtorrent-bin>=1.2.9' #;platform_system=="Linux" and platform_machine=="x86_64"'
		#,"python-apt"#is from 2012 0.7.8, missing DistUtilsExtra, sudo apt install python-apt is 2.2., verify with pip3 install python-apt
	],
	#extras_require={
	#	'bin': ['python-libtorrent-bin>=1.2.9']
	#	#,'apt': ['python-apt']
	#},
	description='Torrent client',
	long_description=README,
	long_description_content_type="text/markdown",
	url='https://github.com/colin-i/tora',
	author='cb',
	author_email='costin.botescu@gmail.com',
	license='MIT',
	entry_points = {
		'console_scripts': [pkname+'='+pkname+'.main:main']
	}
)
