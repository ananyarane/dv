print("Enter a number")
n = int(input())
s1 = 0 
s2 = 0
s3 = 0

s1 = (n*(n+1))/2

c = 1
a = 3

while(c<=n):
	s2 = s2 + a
	a = a + 2
	c = c + 1

a = 1
c = 1

while (c <= n):
	if int(a**0.5) * int(a**0.5) == a:
		a = a + 1
		continue
	else:
		s3 = s3 + a
		c = c + 1
		a = a + 1

print(s1)
print(s2)
print(s3)
