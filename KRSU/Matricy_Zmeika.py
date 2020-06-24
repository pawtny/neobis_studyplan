n, m = map(int, input().split())
a = [list(map(int, input().split())) for i in range(n)]

u = 0
r = 0
l = 0
d = 0

while u + d < n and r + l < m:
    for i in range(l, m - r):
        print(a[u][i], end = " ")
    print()
    u += 1

    for i in range(u, n - d):
        print(a[i][n - r], end = " ")
    print()
    r += 1

    for i in range(m - r - 1, l - 1, -1):
        print(a[n - d - 1][i], end = " ")
    print()
    d += 1

    for i in range(n - d - 1, u - 1, -1):
        print(a[i][l], end = " ")
    print()
    l += 1
