n, m = map(int, input().split())
a = [list(map(int, input().split())) for i in range(n)]

for i in range(m):
    for j in range(n):
        print(a[n - j - 1][i], end = " ")
    print()
