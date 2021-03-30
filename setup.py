
reqs='python-libtorrent>=2.0.2'
from os import uname
if uname().machine!='armv7l':
	reqs='python-libtorrent-bin>=2.0.2'

import pathlib
HERE = pathlib.Path(__file__).parent
README = (HERE / "README.md").read_text()

from setuptools import setup
setup(name='tora',
	install_requires=[reqs],
	version='1.0.0',
	description='Torrent client',
	long_description=README,
	long_description_content_type="text/markdown",
	url='https://github.com/colin-i/tora',
	author='bot',
	author_email='costin.botescu@gmail.com',
	license='MIT',
	packages=['tora'],
	zip_safe=False,
	entry_points = {
		'console_scripts': ['tora=tora.main:main']
	}
)
