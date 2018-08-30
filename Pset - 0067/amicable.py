x = 2
ami = []
sum1 = 0
def sumofdivisors(n):
    sum = 0
    for i in range(1,n):
        if n%i == 0:
            sum = sum + i
    return sum

while x<10000:
    div1 = sumofdivisors(x)
    div2 = sumofdivisors(div1)
    if x == div2 and (not div1 in ami) and div1 != div2:
        ami.append(x)
        ami.append(div1)
        sum1 = sum1 + x + div1
    x = x + 1

print(sum1)