sum = 0
n1 = 9
a = 5



while(n1<=1002001):
	sum = sum + n1 
	n1 = a ** 2
	#n4 = (a ** 2) - d
	a = a + 2
	#d = d + 6

n3 = 7
b = 2
c = 5

while(n3<=1001001):
	sum = sum + n3
	n3 = (4*b*b) + c
	b = b + 1
	c = c + 2


n2 = 5
b = 2

while(n2<=1000001):
	sum = sum + n2 
	n2 = (4 * b * b) + 1
	#n3 = (4 * b * b) + c
	b = b + 1
	#c = c + 2


n4 = 3
a = 5
d = 12

while (n4 <= 999001):
	sum = sum + n4
	n4 = (a**2) - d
	a = a + 2
	d = d + 6



sum = sum + 1
print(sum)