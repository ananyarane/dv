import random

print("Enter a limit")
m = int(input())
cnt = 1
y = random.randint(1,m)

while True:
	print("Enter a guess")
	n = int(input())
	if n > y:
		print("High")
		cnt = cnt + 1
	elif n < y:
		print('Low')
		cnt = cnt  + 1
	elif y == n :
		break

print("Correct!")
print("Number of attempts: "+str(cnt))