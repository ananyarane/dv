n = []
cnta = 0
cntd = 0

print("Enter five numbers")
for i in range(5):
	x = int(input())
	n.append(x)

for i in range(5):
	for j in range(i+1,5):
		if n[i]<n[j]:
			cnta = cnta + 1
		else:
			cntd = cntd + 1
		


if cnta == 10:
	print("Ascending!")
elif cntd == 10:
	print("Descending")
else:
	print("None!")