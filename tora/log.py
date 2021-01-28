
try:
	from . import gtk
	from . import torrent
except Exception:
	import gtk
	import torrent
k=gtk.k

#in case config file is not yet created
log_bf=k.gtk_entry_buffer_new(None,-1)
f=None

def store(d):
	d['log_file']=finish()
def restore(d):
	log=d['log_file']
	if len(log)>0:
		k.gtk_entry_buffer_set_text(log_bf,log.encode(),-1)
		global f
		f=open(log,"w")

def add(ratio):
	if f:
		f.write("\n")
		for x in torrent.torrents:
			s=x.h.status()
			u=x.u+s.total_payload_upload#if pause this will be 0, all_time_upload
			f.write(str(u)+"\n")
		f.write(str(ratio)+"\n")
		f.flush()

def addT(path):
	if f:
		f.write(path+"\n")

def finish():
	global f
	if f:
		f.close()
		f=None
	return k.gtk_entry_buffer_get_text(log_bf).decode()
def reset():
	d=finish()
	if len(d)>0:
		global f
		f=open(d,"a")
