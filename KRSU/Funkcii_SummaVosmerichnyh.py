a, b = map(int, input().split())

def reverse(s):
    n = "0"
    for i in range(len(s) - 1, -1, -1):
        n += s[i]
    return n

def toDesyat(n):
    desyat = 0
    k = 0
    while n > 0:
        desyat += n % 10 * 8 ** k
        n //= 10
        k += 1
    
    return desyat

def toVosem(n):
    vosemRev = ""
    
    while n > 0:
        vosemRev += str(n % 8)
        n //= 8
    return int(reverse(vosemRev))

print(toVosem(toDesyat(a) + toDesyat(b)))