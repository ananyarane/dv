orig = []

def reverse_sum_and_check_equality(x):
    orig = list(x)
    sumforward = 0
    sumreverse = 0
    for i in orig:
        sumforward = int(sumforward) + int(i)
        sumreverse = int(i) + int(sumreverse)

    if sumforward == sumreverse:
        return True
    else:
        return False


print ("Enter a number")
n = input()
returnedtrue = reverse_sum_and_check_equality(n)
if returnedtrue:
    print(True)
else:
    print(False)
