print("Enter three numbers")
x = int(input())
y = int(input())
z = int(input())

if x>y and x>z:
    if x**2 == y**2 + z**2:
        print("True")
    else:
        print("False")

elif y>x and y>z:
    if y**2 == x**2 + z**2:
        print("True")
    else:
        print("False")

else:
    if z**2 == x**2 + y**2:
        print("True")
    else:
        print("False")
