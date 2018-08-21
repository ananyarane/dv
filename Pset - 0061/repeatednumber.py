
n = []
cnt = int(1)
n = [1,2,3,4,1,2,3,5,6,4]

for i in range(10):
    cnt = int(1)
    for j in range((i+1),10):
        if n[i] == n[j] and n[i] != 0:
            n[j]=0
            cnt= cnt+1
    if cnt>1:
        print(str(n[i]))
