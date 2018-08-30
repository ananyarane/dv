n = [4]
terms = 0
cnt = 0
for i in range(2,101):
    for j in range(2,101):
        p = i ** j
        n.append(p)

for i in range(len(n)):
    for j in range(i+1,len(n)):
        if n[i]==n[j]:
            n[j]=0

for i in range(len(n)):
    if n[i]!=0:
        cnt = cnt + 1


print (cnt)
