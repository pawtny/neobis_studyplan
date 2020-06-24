n, m = map(int, input().split())
a = [list(map(int, input().split())) for i in range(n)]
b = [[0] * m for i in range(n)]

for i in range(n):
    for j in range(m):
        b[j][i] = a[i][j]

for i in b:
    print(" ".join(map(str, i)))

