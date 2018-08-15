orig = []

def findSumOfDigits(x):
  orig = list(x)
  sum = 0
  for i in orig:
      sum  = int(sum) + int(i)

  return sum

print("Enter two numbers")
x = input()
y = input()

sum1 = findSumOfDigits(x)
sum2 = findSumOfDigits(y)

if sum1 == sum2:
    print("1")
else:
    print("0")
