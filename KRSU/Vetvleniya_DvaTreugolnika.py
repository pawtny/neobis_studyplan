import math

x1, y1, x2, y2, x3, y3 = map(int, input().split())
a1, b1, a2, b2, a3, b3 = map(int, input().split())
a = [0, 0, 0]
b = [0, 0, 0]

a[0] = math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
a[1] = math.sqrt((x2 - x3) ** 2 + (y2 - y3) ** 2)
a[2] = math.sqrt((x1 - x3) ** 2 + (y1 - y3) ** 2)

b[0] = math.sqrt((a1 - a2) ** 2 + (b1 - b2) ** 2)
b[1] = math.sqrt((a2 - a3) ** 2 + (b2 - b3) ** 2)
b[2] = math.sqrt((a1 - a3) ** 2 + (b1 - b3) ** 2)
for i in range(0, 3):
    for j in range(0, 3):
        if a[i] == b[j]:
            b[j] = -1
            break
if b[0] + b[1] + b[2] == -3:
    if math.sqrt(a[0] ** 2 + a[1] ** 2) == a[2] or math.sqrt(a[1] ** 2 + a[2] ** 2) == a[0] or math.sqrt(a[0] ** 2 + a[2] ** 2) == a[1]:
        print("YES")
    else:
        print("NO")
else:
    print("NO")