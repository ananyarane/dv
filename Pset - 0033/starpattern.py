def starPattern():
	cnt = n
	for i in range(n,-1,-1):
		for j in range(cnt):
			print("*",end=' ')
		cnt = cnt - 1
		print()

print("Enter a number")
n = int(input())
starPattern()
