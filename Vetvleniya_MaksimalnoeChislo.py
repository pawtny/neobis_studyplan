a, b, c = map(int, input().split())
if a == b and b == c and a == c:
    print("Same age")
elif a != b and b != c and a != c:
    if a > b and a > c:
        print("Anton")
    elif b > a and b > c:
        print("Boris")
    else:
        print("Victor")
else:
    if a < b and a < c:
        print("Anton")
    elif b < a and b < c:
        print("Boris")
    else:
        print("Victor")