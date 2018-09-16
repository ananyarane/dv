import math
def isprime(x):
	c = 0
	h = int(x**0.5)
	for i in range(2,h+1):
		if(x%i == 0):
			c  = c + 1

	if c == 0:
		return True
	else:
		return False

n = 0 
flag = True
s = 0
ln= 0 
ca = 0
cb = 0

for a in range(-999,1000):
	if a==2 or a%2 !=0:
		for b in range(-1000,1001):
			n = 0
			if not isprime(abs(b)):
				continue
			
			else:
				s = n*n + a*n + b
				while isprime(abs(s)):
					s = n*n + a*n + b
					n = n + 1

			if n > ln:
				ln = n
				ca = a
				cb = b
	else:
		continue
ln = ln - 1
print("Longest sequence: "+str(ln))
print("a= "+str(ca))
print("b= "+str(cb))