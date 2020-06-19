n = int(input())
a = list(map(int, input().split()))
x = int(input())
mini = a[0]

for i in range(0, n):
    if max(a[i], x) - min(a[i], x) < max(mini, x) - min(mini, x):
        mini = a[i]

print(mini)