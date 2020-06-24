n, x = map(int, input().split())
a = list(map(int, input().split()))
a.sort()

l = 0
r = n
c = 0
while (l < r - 1):
    m = (l + r) // 2
    c += 1
    if(a[m] == x):
        l = m
        break
    elif a[m] > x:
        r = m
    else:
        l = m

for i in a:
    print(i, end = " ")
print()
if a[l] == x:
    print("YES", c)
else:
    print("NO", c)