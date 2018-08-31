n = []
import math
print("Enter a list of 10 numbers")
for i in range (10):
    x = int(input())
    n.append(int(x))

diff = abs((n[1]-n[0]))
a = n[0]
b = n[1]



for i in range(9):
    if abs(n[i+1]-n[i]) < diff:
        diff = abs((n[i+1]-n[i]))
        a = n[i]
        b = n[i+1]

print()
print(a)
print(b)
