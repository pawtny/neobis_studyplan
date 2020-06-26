n, m = map(int, input().split())
a = [list(map(int, input().split())) for i in range(n)]
b = [[0] * m for i in range(n)]

j = 0
x = 0
y = 0
while True:
    for k in range(n):
        b[x][y % m] = a[j // m][j % m]
        x += 1
        j += 1
    if j < n * m:
        y += 1
        x -= 1
        for k in range(n):
            b[x][y % m] = a[j // m][j % m]
            x += -1
            j += 1
    if j < n * m:
        y += 1
        x += 1
    else:
        break

for i in b:
    print(" ".join(map(str, i)))
# WA on test 4 