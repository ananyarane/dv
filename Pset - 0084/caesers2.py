i = 1
j = 0
e = ''
print("Enter an encrypted message")
x = input()
x = x.upper()

print("Enter the key")
n = int(input())

for i in range(len(x)):
    c = ord(x[i])
    if c >= 65 and c <= 90:
        if(c > 65 + (n-1)):
            c = c - n
            e = e + chr(c)
        else:
            p = (65 + (n-1)) - c
            e = e + chr(90-p)
    else:
        e = e + x[i]

print("Encrypted message")
print(e)
