n, x = map(int, input().split())
a = list(map(int, input().split()))
sett = {-1,}

for i in range(0, n):
    sett.add(a[i] % x)

print(len(sett) - 1)
