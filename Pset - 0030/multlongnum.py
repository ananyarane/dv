print("Enter two numbers")
n1 = input()
n2 = input()

c = 0
z = 0
ans = ''
finans = 0
sans = ''

for i in range(len(n1)-1,-1,-1): #loop from last digit of first number, to the first
	c = 0 
	ans = '' #answer per row of multiplication, so it is an empty string in the beginning
	for j in range(len(n2)-1,-1,-1): #loop from last digit of second number, to the first
		p = c + (int(n2[j]) * int(n1[i])) #product of each corresponding digit (adding the carried forward value of the previous digits)
		p1 = str(p % 10) #finding the last digit of the answer above
		ans = p1 + ans #concating only that to the final answer
		c = int(p / 10) #finding the carried forward value
		if j == 0:
			ans = str(c) + ans #for the last iteration of the j loop, the even the carried forward value gets added
	for k in range(z):
		ans = ans + "0" #adding zeros to the end based on the row, ie, 1 for the second, 2 for the third etc
	z = z + 1 
	ians = int(ans)
	finans = finans + ians #adding it to the final answer

print("Answer: "+str(finans))