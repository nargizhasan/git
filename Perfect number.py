Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 20:34:20) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> Number = int(input(" Enter any number: "))
 Enter any number: 13
>>> Sum = 0
>>> for i in range(1, Number):
	if (Number % i == 0):
		Sum = Sum + i
	if (Sum == Number):
		print (" %d is a perfect number" %Number)
	else:
		print(" %d is a not perfect number" %Number)
		
