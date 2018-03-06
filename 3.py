def divide(a,b):
	try:
		return True,a/b
	except ZeroDivisionError:
		return False,None
print (divide(10,0))