a, b, c = map(int, input().split())
o = 0
if a == b and b == c and a == c:
    print(3)
elif a != b and b != c and a != c:
    print(1)
else:
    print(2)