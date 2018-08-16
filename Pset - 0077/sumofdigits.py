orig = []

print("Enter a number")
n = input()

orig = list(n)
sum = 0
for i in orig:
    sum  = int(sum) + int(i)

print("Sum of digits: " + str(sum))
