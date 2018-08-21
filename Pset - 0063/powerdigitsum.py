
n = int(2 ** 1000)
n = str(n)

orig = list(n)
sum = 0
for i in orig:
    sum  = int(sum) + int(i)

print("Sum of digits: " + str(sum))
