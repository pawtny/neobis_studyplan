import random

n, b = map(int, input().split())
a = list([0] * n)
for i in range(0, n - 1):
    a[i] = random.randint(0, 5)
    print(a[i], "", end = "")
else:
    a[-1] = random.randint(0, 4)
    print(a[-1])

for i in range(0, n):
    if a[i] == b:
        print(i)