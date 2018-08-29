n = 1
flag = True
i = 1
flag1 = True
while flag1 == True:
    n = n + 1
    i = 1
    flag = True
    while i < 21 and flag == True:
        s = n%i
        if s != 0:
            flag = False
        elif i == 20:
            flag1 = False
            break
        else:
            i = i +1


print (n)
