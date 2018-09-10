print("Enter the limit")
n = int(input())
a = [1]
b = []
x = 1
ind = int((2*n-1)/2)
print(ind)
cnt = 0


while x<=n:
	p = 0
	q = 0
	for i in range(0,ind-cnt):
		print(" ",end='')

	for i in range(ind-cnt,ind+cnt+1):
		if q%2 == 0:
			print(str(a[p]),end='')
			p = p + 1
		else:
			print(" ",end = '')
		q = q + 1
		
	for i in range(ind+cnt+1,2*n-1):
		print(" ",end = '')

	print()
	cnt = cnt + 1
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
