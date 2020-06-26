n = int(input())
a = list(map(int, input().split()))

for i in range(1, n):
    k = a[i]
    j = i - 1
    boo = False
    while j >= 0 and k < a[j]:
        a[j + 1] = a[j]
        j -= 1
        boo = True
    a[j + 1] = k
    if boo:
        for i in a:
            print(i, end = " ")
        print()