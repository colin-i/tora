
import bencode

def add(filename):
	with open(filename,'rb') as f:
		d=f.read()
		cod=bencode.decode(d)
		return cod[0][b'info'][b'name']