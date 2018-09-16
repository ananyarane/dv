a = 1
s = ''
m = 0
lm = 0
lb = 0
cnt = 1
lcnt = 0
mcnt = 0

for b in range(2,1001):
	s = []
	m = 0 
	a = 1
	while m < 1001:
		c = int(a/b)
		s.append(str(c))
		a = a - (b*c)
		a = a * 10	
		m = m + 1
	s = s[1:]
	#print(s)
	for i in range(len(s)-3):
		cnt = 0
		for j in range(i+1,len(s)-2):
			if s[i] == s[j] and s[i+1] == s[j+1] and s[i+2] == s[j+2]:
				'''print("i      "+str(i))
				print("j      "+str(j))
				print("s[i]   "+str(s[i]))
				print("s[i+1] "+str(s[j]))
				print("s[j]   "+str(s[i+1]))
				print("s[j+1] "+str(s[j+1]))'''
				cnt = j - i
				break
		if cnt > mcnt:
			mcnt = cnt

	if mcnt > lcnt:
		lcnt = mcnt 
		lb = b
		#break


print(lb)


