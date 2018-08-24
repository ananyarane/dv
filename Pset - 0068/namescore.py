f = open("names.py","r+")
from names import namelist as n

totalscore = 0

l = len(n)

for i in range(0,l-1):
    for j in range(0,l-i-1):
        if(n[j]>n[j+1]):
            temp = n[j]
            n[j] = n[j+1]
            n[j+1] = temp


for i in range(l):
    count = 0
    word = n[i]
    for j in range(len(word)):
        a = ord(word[j])
        count = count + (a - 64)
    pos = i+1
    score = count * pos
    totalscore = totalscore + score

print(totalscore)
