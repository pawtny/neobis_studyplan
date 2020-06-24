n, k = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

for x in b:
    l = 0
    r = n - 1
    while (l < r):
        m = (l + r) // 2
        if a[m] < x:
            l = m + 1
        else:
            r = m

    if l > 0 and a[l] != x and abs(a[l - 1] - x) <= abs(a[l] - x):
        print(a[l - 1])
    else:
        print(a[l])
