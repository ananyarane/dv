
p = 0
lp = 0
def palin(x):
    rev = ''
    for i in range(len(x)-1,-1,-1):
        rev = rev + x[i]

    if x == rev:
        return True
    else:
        return False


for i in range(100,1000):
    for j in range(100,1000):
        p = i * j
        if palin(str(p)) and p > lp:
            lp = p


print (lp)
