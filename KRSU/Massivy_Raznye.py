n = int(input())
a = list(map(int, input().split()))
a.sort()
c = 1

for i in range(1, n):
    if a[i -1] != a[i]:
        c += 1
        
print(c)