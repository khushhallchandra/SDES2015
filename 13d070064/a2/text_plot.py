import math
def text_plot(x,y,s_x=80,s_y=30):
	"""
	This functions plots the given lists values . It assumes the x entries
	to be positive and y entries can be positive or negative . Data are 
	entered as floating point numbers.Ex- x[i]=4 should be x[i]=4.0
	That is only first and fourth quadrant are plotted. This plot will
	span the given screen area.
	"""
	print "-" * s_x
	x_ratio=(s_x/max(x))
	y_ratio=s_y/(2*max(y))
	for i in range(len(x)):
		x[i]=int(x[i]*x_ratio)
	for i in range(len(y)):
		y[i]=int(y[i]*y_ratio)
	for i in range(s_y/2,(-s_y/2)-1,-1):
		dummy_x=[]
		for j in range(len(y)):
			if i==y[j]:
				dummy_x.append(x[j])
		dummy_x=sorted(dummy_x)

		for k in range((s_x)):

			for p in range(len(dummy_x)):
				if k==dummy_x[p]:
					print "*",
			print "",	
		print ""
	print "-" * s_x
def testrun():
	"""
	This function is used for sample run. The given values 
	correspond to sine values.
	"""
	x=[]
	y=[]
	for i in range(100):
		x.append(.157*i)
	for i in range(len(x)):
		y.append(math.sin(x[i]))
	text_plot(x,y)		
testrun()