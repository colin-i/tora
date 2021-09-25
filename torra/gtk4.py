import apt

def version():
	c=apt.Cache()
	d=c['libgtk-4-bin']
	e=d.versions
	f=e.keys()
	g=e[len(f)-1]
	h=g.dependencies
	k="libgtk-4-"
	l=len(k)
	for i in h:
		j=i.installed_target_versions
		for m in j:
			n=m.package.name
			try:
				o=n.index(k)#ValueError
				if len(n)>l:
					p=n[l:]
					q=int(p)#ValueError
					return p
			except Exception:
				pass
	return None
