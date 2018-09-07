a = []
print("Enter 10 numbers with a decimal point")
for i in range(10):
	x = float(input())
	a.append(x)

sum = 0
for i in a:
	sum = sum + i

avg = sum / 10

print()
print(avg)