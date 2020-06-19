fraction = list(map(int, input().split()))

def gcd(a, b):
    if a == 0:
        return b
    return gcd(b % a, a)

def reduce(fraction):
    divisor = gcd(fraction[0], fraction[1])
    fraction[0] //= divisor
    fraction[1] //= divisor

reduce(fraction)
print("{}/{}".format(fraction[0], fraction[1]))