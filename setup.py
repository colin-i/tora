from setuptools import setup

setup(name='tora',
      version='0.1',
      description='Torrent client',
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
