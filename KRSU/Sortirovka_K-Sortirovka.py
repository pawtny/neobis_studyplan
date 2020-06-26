n = int(input())
a = list(map(int, input().split()))
k = int(input())
c = 0

for i in range(k, n):
    for j in range(k, n):
        if a[j] < a[j - k]:
            a[j], a[j - k] = a[j - k], a[j]
            c += 1

for i in range(n - 1):
    if a[i] > a[i + 1]:
        c = -1
        break
print(c)