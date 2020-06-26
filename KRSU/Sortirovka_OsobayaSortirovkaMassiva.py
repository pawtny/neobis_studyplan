n = int(input())
a = list(map(int, input().split()))
x = a[0 : len(a) // 2]
y = a[len(a) // 2 : len(a)]
x.sort()
y.sort(reverse = True)
a = x + y
print(" ".join(map(str, a)))