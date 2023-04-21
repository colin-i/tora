from . import gtk
from . import torrent
from . import ratio
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

def ini():
	grid = k.gtk_grid_new ()
	k.gtk_grid_attach(grid,ratio.text(b"Max uploads (-1 infinite)"),0,0,1,1)
	k.gtk_grid_attach(grid,ratio.edit(slot_bf),1,0,1,1)
	k.gtk_grid_attach(grid,ratio.text(b"Max connections (-1 infinite)"),0,1,1,1)
	k.gtk_grid_attach(grid,ratio.edit(con_bf),1,1,1,1)
	#
	fr=k.gtk_frame_new(b"Maximum limits")
	k.gtk_frame_set_child(fr,grid)
	return fr
