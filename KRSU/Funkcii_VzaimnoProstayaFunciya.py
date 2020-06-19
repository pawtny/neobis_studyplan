a, b = map(int, input().split())

def gcd(a, b):
    if a == 0:
        return b
    return gcd(b % a, a)

def isVzaimka(a, b):
    return gcd(a, b) == 1

if isVzaimka(a, b):
    print("YES")
else:
    print("NO")