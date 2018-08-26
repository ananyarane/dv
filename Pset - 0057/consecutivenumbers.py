cnt = 1

print("Enter a number")
n = int(input())

for i in range(n):
    for j in range(i+1):
        print(str(cnt),end=" ")
        cnt = cnt + 1
    print()
