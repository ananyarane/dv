f = open("digit.py","r+")
from digit import a as dig

sum = 0

for i in dig:
	sum = sum + i

sum = str(sum)

for i in range(10):
	print(sum[i],end='')