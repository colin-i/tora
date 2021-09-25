#setuptools.setup is looking at one argv parameter; to "build" and "install":
#python3 setup.py install

pkname='torra'

import pathlib
HERE = pathlib.Path(__file__).parent
README = (HERE / "README.md").read_text()

from setuptools import setup
setup(name=pkname,
	version='1.0.23',
	packages=[pkname],
	#opt
	python_requires='>=3',
	install_requires=["appdirs>=1.4.3"
		,"python-apt>=2.2.1"
		#,'python-libtorrent-bin;platform_system=="Linux" and platform_machine=="x86_64"'
	],
	extras_require={
		'bin': ['python-libtorrent-bin>=1.2.9']
	},
	description='Torrent client',
	long_description=README,
	long_description_content_type="text/markdown",
	url='https://github.com/colin-i/tora',
	author='bot',
	author_email='costin.botescu@gmail.com',
	license='MIT',
	entry_points = {
		'console_scripts': [pkname+'='+pkname+'.main:main']
	}
)
