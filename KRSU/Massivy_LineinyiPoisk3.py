n = int(input())
a = list(map(int, input().split()))
x = int(input())

for i in range(0, n):
    if a[i] == x:
        print(i + 1)