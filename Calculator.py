Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 20:34:20) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> def calc(x,o,y):
	if o=='*':
		c=x*y
	elif o=='+':
		c=x+y
	elif o=='-':
		c=x-y
	elif o=='/':
		c=x/y
	else:
		c="Operatoru duzgun daxil edin:"
	return c
#calculator
