#REJECTED

a = list(map(int, input().split()))
b = list.copy(a)
del b[0]
b.sort()

for i in range(1, len(a)):
    if a[i] == b[-1]:
        a[i] = b[0]

print(a[i], end = "")

for i in range(2, len(a)):
    print("" ,a[i], end = "")