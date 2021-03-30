from . import gtk
from . import overall
from . import layout
from . import log
k=gtk.k

ratint_bf=k.gtk_entry_buffer_new(b"0",-1)
ratlim_bf=k.gtk_entry_buffer_new(b"2",-1)
timer=0

def text(a):
	tx=k.gtk_label_new(a)
	k.gtk_widget_set_halign(tx,gtk.GtkAlign.GTK_ALIGN_START)
	return tx
def edit(b):
	e=k.gtk_entry_new_with_buffer(b)
	k.gtk_widget_set_hexpand(e,True)
	return e

def ini():
	grid = k.gtk_grid_new ()
	k.gtk_grid_attach(grid,text(b"Interval time to verify in minutes (0=disable)"),0,0,1,1)
	k.gtk_grid_attach(grid,edit(ratint_bf),1,0,1,1)
	k.gtk_grid_attach(grid,text(b"Value"),0,1,1,1)
	k.gtk_grid_attach(grid,edit(ratlim_bf),1,1,1,1)
	#
	fr=k.gtk_frame_new(b"Close program when Ratio is greater than Value and torrents checking was done")
	k.gtk_frame_set_child(fr,grid)
	return fr

def freeint():
	global timer
	if timer>0:
		k.g_source_remove(timer)
		timer=0
def setint(window):
	freeint()
	gain(window)

@gtk.CALLBACKi
def fresh(window):
	ratio=getratio()
	log.add(ratio)
	n=float(k.gtk_entry_buffer_get_text(ratlim_bf))
	if ratio>n:
		print("Ratio limit. Window close.")
		timer=0
		k.gtk_window_close(window)#it is freeint inside here
		return False
	return True
def gain(w):#when add tor and resets(including log file)
	global timer
	if timer==0:
		n=int(k.gtk_entry_buffer_get_text(ratint_bf))
		if n>0:
			timer=k.g_timeout_add(n*60000,fresh,w)
	log.likenew()

def getratio():
	z=gtk.c_char_p()
	gtk.gtk_tree_model_get(overall.list,overall.it,layout.COLUMNS.RATIO,gtk.byref(z))
	r=float(z.value)
	k.g_free(z)
	return r

def store(d):
	d['ratio_time']=int(k.gtk_entry_buffer_get_text(ratint_bf))
	d['ratio_limit']=float(k.gtk_entry_buffer_get_text(ratlim_bf))
def restore(d):
	a=str(d['ratio_time']).encode()
	k.gtk_entry_buffer_set_text(ratint_bf,a,-1)
	a=str(d['ratio_limit']).encode()
	k.gtk_entry_buffer_set_text(ratlim_bf,a,-1)
