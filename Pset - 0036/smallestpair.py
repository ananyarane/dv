n =[]
print("Enter a list of 10 numbers") #accepting lis tof 10 numbers
for i in range (10):
    x = int(input())
    n.append(int(x))

n1 = n[0] #setting smallest pair to first and second elements
n2 = n[1]
ind = 0
for i in range(0,len(n)): #finding the smallest number of the list
	if n[i] < n1:
		n1 = n[i]
		ind = i #storing the index of the smallest number

for j in range(0,len(n)): #finding the second largest element
	if n[j] < n2: 
		if n[j] == n1 and j == ind: #special case for if the second element is the second smallest and the first element is the smallest
			continue
		elif n[j] == n1 and j != ind: #case for if there's are two of the smallest numbers
			n2 = n[j]
		else:
			n2 = n[j] #any other case
 


print("Smallest pair:")
print (n1)
print (n2)