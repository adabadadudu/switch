def switch(switch,cases,default=None):
	if default:
		return cases.get(switch,default)
	return cases.get(switch)
