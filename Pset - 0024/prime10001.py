n = 13
flag = True
c = 1
import math
i = 1

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

while i <= 10001:
    c = c + 1
    prime = isprime(c)
    if prime:
        i = i + 1

print(c)
