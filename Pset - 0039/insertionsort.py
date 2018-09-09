a = []
print("Enter a list of 10 numbers")
for i in range(10):
	x = int(input())
	a.append(x) #input

#dividing the list into sorted and unsorted parts

for i in range(1,len(a)): #checking the entire list
	key = a[i] #with the element at position i
	j = i - 1 #checking the elements to the left of the current element
	while j >= 0 and a[j] > key: #if an element smaller to the current element is found, the element is moved to the right
		a[j+1] = a[j]
		j = j - 1
	a[j+1] = key #the current element is placed in its correct place in the sorted part of the list
	

print(*a, sep = ' ')