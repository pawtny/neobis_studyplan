n = int(input())
a = list(map(int, input().split()))
a.sort()
x = set(a)

print(len(x))
print(" ".join(map(str, a)))