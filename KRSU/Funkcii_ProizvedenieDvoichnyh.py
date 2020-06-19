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
        desyat += n % 10 * 2 ** k
        n //= 10
        k += 1
    
    return desyat

def toDva(n):
    dvaRev = ""
    
    while n > 0:
        dvaRev += str(n % 2)
        n //= 2
    return int(reverse(dvaRev))

print(toDva(toDesyat(a) * toDesyat(b)))