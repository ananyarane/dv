
'''After many changes, I figured that I could reduce the number of iterations to at least half by increasing count by 2 each time 
because 28 has factors 1,2,4,7,14,28 and 1*28,2*14 etc can be found just once. Till the square root of n, there are half of the total number of factors.
Except, if the number is a perfect square, the square root doesn't get counted while going from 1 -> n**0.5.4
	So I added 1 to the count.
'''
def sumofdivisors(n): 
	
	cnt = 0
	for i in range(1,int(n**0.5)): #initially I changed the limit to n/2, but it wasn't helping.
		if n%i == 0:
			cnt = cnt + 2

	if int(n*0.5) * int(n*0.5) == n: #special case for a perfect square
		cnt = cnt + 1

	return cnt

''' I figured I couldn't use this function because the answer was generated in this function, and then I couldn't access it in the main function. So i just m
	moved the statements from this function into the main'''
'''def sumofnum(n):
	sum = int((n * (n + 1)) / 2)
	numofdiv = sumofdivisors(sum)
	return numofdiv'''
	
n = 1
while True:
	sum = int((n * (n + 1)) / 2)
	div = sumofdivisors(sum)
	if div > 500:
		break
	n = n + 1
	
print(sum)


