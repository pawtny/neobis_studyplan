n = int(input())
a = list(map(int, input().split()))
x, j = map(int, input().split())

a.insert(j - 1, x)

print(" ".join(map(str, a)))