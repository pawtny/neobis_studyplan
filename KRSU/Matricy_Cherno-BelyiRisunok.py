n = int(input())
a = [list(map(int, input().split())) for i in range(n)]
s = 0

for i in range(n):
    for j in range(n):
        s += a[i][j]
s = round(s / (n * n))

for i in range(n):
    for j in range(n):
        if a[i][j] < s:
            a[i][j] = 0
        else:
            a[i][j] = 255

for i in a:
    print(" ".join(map(str, i)))