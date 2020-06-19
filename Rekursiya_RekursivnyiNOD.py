"""a, b = map(int, input().split())

def gcd(x, y):
    a = min(x, y)
    b = max(x, y)
    if a == 0:
        return b
    print("GCD(%d,%d)" % (b - a, a))
    return gcd(b - a, a)

print("GCD(%d,%d)=%d" % (a, b, gcd(a, b)))
Run-time error"""

a, b = map(int, input().split())
d = a
g = b
while a != 0:
    x = a
    y = b
    a = min(x, y)
    b = max(x, y)
    print("GCD(%d,%d)" % (b - a, a))
    c = a
    a = b - a
    b = c



print("GCD(%d,%d)=%d" % (d, g, b))
#kaif