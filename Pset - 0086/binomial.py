a = [1] #take the first element to be 1
b = []
x = 1

print("Enter a number")
n = int(input())

if n == 0 :
	print("0") #if zero, answer is zero

else:
	
	while x<=n:
		a.insert(0,0) #insert a 0 at the beginning of the list
		a.append(0) #insert a 0 at the end of the list
		del b[:] #empty the elements of list b

		for i in range(len(a)-1):
			j = i + 1
			b.append(a[i] + a[j]) #to list b add elements of list a
			''' for example:
			a = [1,1]
			a after inserting and appending = [0,1,1,0]
			add the 0th element to the 1st element, 1st to 2nd and so on, because 110+011 = 121 and so the subsequent terms can be found like that.
			'''

		for i in range(0,len(b)):
			a[i] = b[i] #reassign them to a, to loop it
		
		a.remove(0) #remove all the zeros
		x = x + 1

	x = n
	y = 0
	i = 0

	#printing
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



