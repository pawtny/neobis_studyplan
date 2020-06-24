n = int(input())

l = 0
r = n - 1
c = 0
while (l < r):
    m = (l + r) // 2
    c += 1
    if n < m:
        l = m + 1
    else:
        r = m

print(c)