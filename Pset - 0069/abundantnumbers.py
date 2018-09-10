
num = 12
abun = []
x = 12
flag = False
flag1 = True
sumfin = 78

def abundant(n):
	sum = 0
	for i in range(1,int(n**0.5)+1):
		if n%i == 0:
			if i != n/i:
				sum = sum + i + int(n/i)
			else:
				sum = sum + i 
			

	sum = sum - n
	if sum > n:

		return True
	else:
		return False



while num<28123:
	flag = abundant(num)
	if flag:
		abun.append(num)
	num = num + 1

sumfin = 1
n = 2



while n<=20161:
	flag = True
	for i in abun:
		if i<n:
			if (n-i) in abun:
				flag = False
				break
		else:
			break

	if flag == True:
		sumfin = sumfin + n
		print(n)
	n = n + 1



print(sumfin)

