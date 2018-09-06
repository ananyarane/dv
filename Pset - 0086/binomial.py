a = [1]
b = []
x = 1

print("Enter a number")
n = int(input())

if n == 0 :
	print("0")

else:
	
	while x<=n:
		a.insert(0,0)
		a.append(0)
		del b[:]
		for i in range(len(a)-1):
			j = i + 1
			b.append(a[i] + a[j])

		for i in range(0,len(b)):
			a[i] = b[i]
		
		a.remove(0)
		x = x + 1

	x = n
	y = 0
	i = 0

	print("(x+y)^"+str(n)+" = ",end='')
	while x >= 0:
		if x == 0:
			if b[i]!=1:
				s = str(b[i])
			else:
				s = ''
			print(s+"y^"+str(y),end = '')
		elif y == 0 :
			if b[i]!=1:
				s = str(b[i])
			else:
				s =''
			print(s+"x^"+str(x)+" + ",end = '')
		else:
			if b[i]!=1:
				s = str(b[i])
			else:
				s =''
			print(s+"x^"+str(x)+"y^"+str(y)+" + ",end='')
		x = x - 1
		y = y + 1
		i = i + 1



