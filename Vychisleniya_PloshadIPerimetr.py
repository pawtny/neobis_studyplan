import math

x1, y1, x2, y2, x3, y3 = map(float, input().split())

a = math.sqrt((x1 - x2) * (x1 - x2) + (y1 - y2) * (y1 - y2))
b = math.sqrt((x2 - x3) * (x2 - x3) + (y2 - y3) * (y2 - y3))
c = math.sqrt((x1 - x3) * (x1 - x3) + (y1 - y3) * (y1 - y3))
p = a + b + c
print(p)
print(math.sqrt(p / 2 * (p / 2 - a) * (p / 2 - b)* (p / 2 - c)))