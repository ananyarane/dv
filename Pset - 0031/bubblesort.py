n = [5,1,4,2,8]
l = len(n)

for i in range(0,l-1):
    for j in range(0,l-i-1):
        if(n[j]>n[j+1]):
            temp = n[j]
            n[j] = n[j+1]
            n[j+1] = temp

print (*n,sep=" ")
