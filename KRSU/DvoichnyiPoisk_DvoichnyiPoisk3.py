n, x = map(int, input().split())
a = list(map(int, input().split()))
a.sort()

l = 0
r = n
c = 0
while (l < r):
    c += 1
    m = (l + r) // 2
    if a[m] < x:
        l = m + 1
    elif a[m] > x:
        r = m - 1
    else:
        l = m
        break
for i in a:
    print(i, end = " ")
print()

if a[l] != x:
    c += 1
    
if l > 0 and a[l] != x and abs(a[l - 1] - x) <= abs(a[l] - x):
    print(a[l - 1], c)
else:
    print(a[l], c)