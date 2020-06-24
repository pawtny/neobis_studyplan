n, m = map(int, input().split())
a = [list(map(int, input().split())) for i in range(n)]
l = 0

for i in range(n):
    for j in range(m):
        if j > l:
            a[i][j] = 0
    l += 1

for i in a:
    print(" ".join(map(str, i)))