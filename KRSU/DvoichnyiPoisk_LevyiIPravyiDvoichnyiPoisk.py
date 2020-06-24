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

    if(a[l] != x):
        print(0)
        continue
    
    print(l + 1, end = " ")

    l = 0
    r = n
    while (l < r):
        m = (l + r) // 2
        if a[m] <= x:
            l = m + 1
        else:
            r = m
    
    print(l)