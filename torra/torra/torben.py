from . import bencod

def name(filename):
	with open(filename,'rb') as f:
		d=f.read()
		cod=bencod.decode(d)
		return cod[0][b'info'][b'name']