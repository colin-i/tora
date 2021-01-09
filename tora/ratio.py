try:
	import gtk
	import overall
	import layout
	import stats
	import torrent
	import log
except Exception:
	from . import gtk
	from . import overall
	from . import layout
	from . import stats
	from . import torrent
	from . import log
k=gtk.k

ratint_bf=k.gtk_entry_buffer_new(b"0",-1)
ratlim_bf=k.gtk_entry_buffer_new(b"2",-1)

def text(a):
	tx=k.gtk_label_new(a)
	k.gtk_widget_set_halign(tx,gtk.GtkAlign.GTK_ALIGN_START)
	return tx
def edit(b):
	e=k.gtk_entry_new_with_buffer(b)
	k.gtk_widget_set_hexpand(e,True)
	return e

def ini(window):
	grid = k.gtk_grid_new ()
	k.gtk_grid_attach(grid,text(b"Interval time to verify in minutes (0=disable)"),0,0,1,1)
	k.gtk_grid_attach(grid,edit(ratint_bf),1,0,1,1)
	k.gtk_grid_attach(grid,text(b"Value"),0,1,1,1)
	k.gtk_grid_attach(grid,edit(ratlim_bf),1,1,1,1)
	#
	fr=k.gtk_frame_new(b"Close program when Ratio is greater than Value and all torrents are seeds")
	k.gtk_frame_set_child(fr,grid)
	return fr

timer=0

def newint(window):
	n=int(k.gtk_entry_buffer_get_text(ratint_bf))
	if n>0:
		global timer
		timer=k.g_timeout_add(n*60000,fresh,window)

def freeint():
	global timer
	if timer>0:
		k.g_source_remove(timer)
		timer=0

def setint(window):
	freeint()
	newint(window)

@gtk.CALLBACKi
def fresh(window):
	log.add()
	ratio=getratio()
	n=float(k.gtk_entry_buffer_get_text(ratlim_bf))
	if ratio>n:
		if are_done():
			k.gtk_window_close(window)
	return True

def getratio():
	z=gtk.c_char_p()
	gtk.gtk_tree_model_get(overall.list,overall.it,layout.COLUMNS.RATIO,gtk.byref(z))
	r=float(z.value)
	k.g_free(z)
	return r

def are_done():
	en=stats.sed()
	for x in torrent.torrents:
		s=x.h.status()
		if s.state!=en:
			return False
	return True

def store(d):
	d['ratio_time']=int(k.gtk_entry_buffer_get_text(ratint_bf))
	d['ratio_limit']=float(k.gtk_entry_buffer_get_text(ratlim_bf))
def restore(d):
	a=str(d['ratio_time']).encode()
	k.gtk_entry_buffer_set_text(ratint_bf,a,-1)
	a=str(d['ratio_limit']).encode()
	k.gtk_entry_buffer_set_text(ratlim_bf,a,-1)
