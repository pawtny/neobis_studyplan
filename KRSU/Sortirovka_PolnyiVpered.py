n = int(input())
a = list(map(int, input().split()))
k = 0

for i in range(n):
    if a[k] < a[i]:
        k = i

a[0], a[k] = a[k], a[0]

print(" ".join(map(str, a)))