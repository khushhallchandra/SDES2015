def gcd(a,b):
	"""Returns the Greatest common divisor 
	of the two argument entered
	The input number should be positive otherwise error will occur
	"""
	a_bool=isinstance(a,(int,long))
	b_bool=isinstance(b,(int,long)) 
	try:
		if (a<0 or b <0 or a_bool==False or b_bool==False):
			raise ValueError()
		if ( not a_bool or  not b_bool):
			raise TypeError()
		if a==0:
			return b
		while b!=0:
			if a>b:
				a=a-b
			else:
				b=b-a
		return a
	except ValueError:
		print "Value error detected"
	except TypeError:
		print "Type error detected"