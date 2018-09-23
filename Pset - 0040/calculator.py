def add(x,y):
    s = x + y

    return s

def subtract(x,y):
    s = x - y

    return s

def multiply(x,y):
    s = x * y

    return s

def divide(x,y):
    s = x/y

    return s


print("Enter two numbers")

x = int(input())
y = int(input())

s1 = add(x,y)
print("Addition: "+str(s1))
s2 = subtract(x,y)
print("Subtraction: "+str(s2))
s3 = multiply(x,y)
print("Multiplication: "+str(s3))
s4 = divide(x,y)
print("Division: "+str(s4))

