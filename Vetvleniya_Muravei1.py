import math

a, b, c = map(int, input().split())
p = a + b
o = c * 2 + math.sqrt(a ** 2 + b ** 2)
if p < o:
    print(p ** 2)
else:
    print(round(o ** 2))