import random
n =[]
c = 0
while True:
    x = random.randint(0,10)
    c = 0
    for j in range(len(n)):
        if x != n[j]:
            c = c+1
    if c == len(n):
        n.append(x)
    if len(n) == 5:
        break

print(*n,sep=" ")
