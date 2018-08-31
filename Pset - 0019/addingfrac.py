
print("Enter the numerator and denominator of two fractions")
print("First fraction:") #input both fractions
num1 = int(input())
den1 = int(input())
print("Second fraction:")
num2 = int(input())
den2 = int(input())

if den1==den2:
	denfin = den1
	numfin = num1 + num2
else:
	denfin = den1 * den2 #calculating the product of the two denominators
	numfin = (num1*den2) + (num2*den1) #finding the numerator by cross multiplying


if numfin%denfin == 0:
	print("Sum: "+str(int(numfin/denfin)))

else:
	print("Sum: "+str(numfin)+"/"+str(denfin))



'''
I'm still working on this but the question doesn't specify this so...

#reducing to the smallest form

if numfin > denfin: #if it is 
	a = numfin
	b = denfin
	print(a)
	print(b)
	s = int(a**0.5) + 1
	for i in range(1,s):
		print(i)

		if a%i == 0 and b%i == 0:
			print("Divisible for :"+str(i))
			a = int(a/i)
			b = int(b/i)
	print("Sum:"+str(a)+"/"+str(b))


elif numfin < denfin:
	a = denfin
	b = numfin
	for i in range(1,int(a**0.5)+1):
		if a%i == 0 and b%i == 0:
			a = int(a/i)
			b = int(b/i)
	print("Sum:"+str(b)+"/"+str(a))

else:
	print("Sum: 1")
'''


