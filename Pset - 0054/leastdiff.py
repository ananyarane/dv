n = []

print("Enter a list of 10 numbers")
for i in range (10):
    x = int(input())
    n.append(int(x))

diff = n[1]-n[0]
a = 0
b = 0

print (*n, sep = " ")

for i in range(9):
    if n[i+1]-n[i] < diff:
        diff = n[i+1]-n[i]
        a = n[i]
        b = n[i+1]

print(a)
print(b)
