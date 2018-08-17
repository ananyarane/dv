
fac = '1'
x = int('100')

while(x>0):
    fac = int(fac) * x
    x = x - 1

orig = []


orig = list(str(fac))
sum = 0
for i in orig:
    sum  = int(sum) + int(i)

print("Sum of digits: " + str(sum))
