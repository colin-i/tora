from . import gtk
from . import torrent
k=gtk.k

slot_bf=k.gtk_entry_buffer_new(b"-1",-1)
con_bf=k.gtk_entry_buffer_new(b"-1",-1)

def store(d):
	d['max_uploads']=getu()
	d['max_connections']=getc()
def restore(d):
	k.gtk_entry_buffer_set_text(slot_bf,str(d['max_uploads']).encode(),-1)
	k.gtk_entry_buffer_set_text(con_bf,str(d['max_connections']).encode(),-1)
	set()

def getu():
	return int(k.gtk_entry_buffer_get_text(slot_bf))
def getc():
	return int(k.gtk_entry_buffer_get_text(con_bf))
def set():
	torrent.ses.set_max_uploads(getu())
	torrent.ses.set_max_connections(getc())
