n, x = map(int, input().split())
a = list(map(int, input().split()))
a.sort()

l = 0
r = n
c = 0
while (l < r - 1):
    c += 1
    m = (l + r) // 2
    if(a[m] == x):
        l = m
        break
    elif a[m] > x:
        r = m
    else:
        l = m

print(" ".join(map(str, a)), end = " \n")
if(a[l] != x):
    print(0, c)
else:
    l = 0
    r = n - 1
    while (l < r):
        m = (l + r) // 2
        if a[m] < x:
            l = m + 1
        else:
            r = m

    l1 = 0
    r1 = n
    while (l1 < r1):
        m = (l1 + r1) // 2
        if a[m] <= x:
            l1 = m + 1
        else:
            r1 = m
    
    print(l1 - l, c)