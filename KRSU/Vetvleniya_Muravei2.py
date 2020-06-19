import math

a, b = map(int, input().split())

a *= 100
b *= 100
x = 150
y = 200
#d = math.floor(math.sqrt(a ** 2 + b ** 2)) #dist from point to the (0 ; 0)
#d1 = math.floor(math.sqrt(x ** 2 + y ** 2)) #dist from the top point of the wall to the (0 ; 0)
#d2 = math.floor(math.sqrt((a - x) ** 2 + (b - y) ** 2)) #dist to the top point of the wall
#d3 = math.floor(math.sqrt((a - x) ** 2 + (b ** 2))) #dist to the bottom point of the wall
d4 = b #dist to the bottom
d5 = math.floor(4 * a / 3 - b) #dist to the top y = 4/3 * x
d6 = math.floor(a - b * 3 / 4) #dist to the left (function)

#print((d2, d3, d4, d5, d6))
if a < x or b <= 0 or d5 <= 0:
    print(0)
else: 
    print(min(d4, d5, d6))
    