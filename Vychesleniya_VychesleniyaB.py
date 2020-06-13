import math

ax, ay = map(float, input().split())
bx, by = map(float, input().split())
dlina = math.sqrt((ax - bx) ** 2 + (ay - by) ** 2)
print( "%.3f" % dlina)