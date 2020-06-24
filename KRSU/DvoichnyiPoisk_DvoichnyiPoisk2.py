n, x = map(int, input().split())
a = list(map(int, input().split()))
a.sort()

l = 0
r = n
c = 0
v = 0
while (l < r - 1):
    m = (l + r) // 2
    c += 1
    if(a[m] == x):
        v += 1
    if a[m] > x:
        r = m
    else:
        l = m

for i in a:
    print(i, end = " ")
print()
print(v, c)