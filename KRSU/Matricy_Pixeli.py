n, m = map(int, input().split())
a = [list(map(int, input().split())) for i in range(n)]
l = 0

for i in range(n // 2):
    a[i], a[n - i - 1] = a[n - i - 1], a[i]

for i in a:
    print(" ".join(map(str, i)))