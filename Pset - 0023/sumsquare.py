
n = 0
sum = 0
sum1 = 0
diff = 0

for i in range(1,101):
    n = i * i
    sum = sum + n
    sum1 = sum1 + i

diff = (sum1 * sum1) - sum

print (str(diff))
