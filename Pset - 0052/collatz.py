n = 1
n1 = n
x = []
cnt = 1
lcnt = 4
while(n1<1000000):
    n = n1
    cnt = 1
    while (n>1):
        if n%2 == 0:
            n = n/2
            cnt = cnt + 1
        else:
            n = 3*n + 1
            cnt = cnt + 1
    if (cnt > lcnt):
        lcnt = cnt
        num = n1
    n1 = n1 + 1

print("Starting number: "+str(num))
