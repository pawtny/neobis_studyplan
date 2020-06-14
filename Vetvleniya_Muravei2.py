import math

a, b = map(int, input().split())

a *= 100
b *= 100
x = 150
d = math.floor(math.sqrt(a ** 2 + b ** 2))
d1 = math.floor(math.sqrt(x ** 2 + 200 ** 2))
d2 = math.floor(math.sqrt((a - 150) ** 2 + (b - 200) ** 2))
d3 = math.floor(math.sqrt((a - 150) ** 2 + (b ** 2)))
d4 = b
d5 = math.floor(4 * a / 3 - b)


if a < x or b <= 0 or d - d1 == d2:
    print(0)
else:
    print(min(d2, d3, d4, d5))
    