n = 600851475143
lf = 1

def isprime(x):
    cnt = 0
    for i in range(1,x+1):
        if(x%i == 0):
            cnt = cnt + 1

    if cnt == 2:
        return True
    else:
        return False


for i in range(1,n+1):
    if(n%i==0):
        flag = isprime(i)
        if flag:
            if i > lf:
                lf = i

print("Largest = "+str(lf))
