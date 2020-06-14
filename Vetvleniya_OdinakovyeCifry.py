a = int(input())
b = a % 10
a //= 10
boo = False
while a > 0:
    if a % 10 == b:
        boo = True
    b = a % 10
    a //= 10

if boo:
    print("YES")
else:
    print("NO")