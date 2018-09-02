print("Ener a number")
p = int(input())
cnt = 0
i = 1
if p < 3:
	print("NO")
else:
	while True:
		if p == 2*i + 1 :
			cnt = cnt + 1
			break
		i = i + 1

if cnt == 1:
	print("YES")
else:
	print("NO")