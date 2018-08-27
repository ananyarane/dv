n = []

for i in range(10):
    print("Enter a number")
    x = int(input())
    n.append(x)

print("Enter a number to search")
x = int(input())

for i in range(10):
    if n[i]==x:
        print("Number found at position "+str(i))
        break
