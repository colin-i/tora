
import bencode

def add(filename):
	with open(filename,'rb') as f:
		d=f.read()
		cod=bencode.decode(d)
		return file