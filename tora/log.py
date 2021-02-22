
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

def div_nr(a,b):
	if not b:
		return 0
	return a/b
def one(x):
	s=x.h.status()
	u=x.u+s.total_payload_upload#if pause this will be 0, all_time_upload
	return div_nr(u,s.total_done)
def add(ratio):
	if f:
		f.write("\n")
		for x in torrent.torrents:
			r=one(x)
			f.write(str(r)+"|"+str(r-x.in_ratio)+"\n")
		f.write(str(ratio)+"|"+str(ratio-in_ratio)+"\n")
		f.flush()
def addT(path):
	if f:
		f.write(path+"\n")

def gain(fn):
	global in_ratio
	in_ratio=fn()
	for x in torrent.torrents:
		x.in_ratio=one(x)

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
