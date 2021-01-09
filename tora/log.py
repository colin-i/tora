
try:
	import gtk
	import torrent
except Exception:
	from . import gtk
	from . import torrent
k=gtk.k

def store(d):
	d['log_file']=k.gtk_entry_buffer_get_text(log_bf).decode()
	if f:
		f.close()

def restore(d):
	log=d['log_file'].encode()
	global log_bf,f
	if len(log)>0:
		log_bf=k.gtk_entry_buffer_new(log,-1)
		f=open(log,"w")
	else:
		log_bf=k.gtk_entry_buffer_new(None,-1)
		f=None

def add():
	if f:
		for x in torrent.torrents:
			s=x.h.status()
			u=x.u+s.total_payload_upload#if pause this will be 0, all_time_upload
			f.write(str(u)+"\n")
		f.write("\n")
		f.flush()
