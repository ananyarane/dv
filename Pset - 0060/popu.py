a = 50*(10**6)
b = 70*(10**6)
cnt = 0

while True:
    a = a+0.03*a
    b = b +0.02*b
    cnt = cnt + 1
    if(a>b):
        break
print(str(a/10**6))
print(str(b/10**6))
print(cnt)
