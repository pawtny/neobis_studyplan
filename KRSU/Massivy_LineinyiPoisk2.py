n = int(input())
a = list(map(int, input().split()))
x = int(input())
s = "NO"

for i in range(0, n):
    if a[i] == x:
        s = "YES"
        break

print(s)