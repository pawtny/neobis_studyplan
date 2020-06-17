a, b = map(int, input().split())

def gcd(a, b):
    if a == 0:
        return b
    return gcd(b % a, a)

def lcm(a, b):
    return a * b // gcd(a, b)

print("GCD", gcd(a, b))
print("LCM", lcm(a, b))