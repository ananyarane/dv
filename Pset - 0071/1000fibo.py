a = 1
b = 1
c = 2 
i = 3 

while True:
	a = b
	b = c 
	c = a + b
	i  = i + 1
	if len(str(c)) == 1000:
		print (i)
		break
		
