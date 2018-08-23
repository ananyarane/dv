sum = 0

def isprime(x):
    cnt = 0
    for i in range(1,x+1):
        if(x%i == 0):
            cnt = cnt + 1

    if cnt == 2:
        return True
    else:
        return False


for i in range(1,2000000):
    if isprime(i):
        print (i)
        sum = sum + i

print (str(sum))
