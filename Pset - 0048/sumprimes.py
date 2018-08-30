sum = 0

def isprime(x):
    cnt = 0
    h = int(x**0.5)
    for i in range(2,h+1):
        if(x%i == 0):
            cnt  = cnt+ 1

    if cnt == 0:
        return True
    else:
        return False


for i in range(1,2000000):
    if i%2!=0:
        if isprime(i):
            sum = sum + i

print (str(sum))
