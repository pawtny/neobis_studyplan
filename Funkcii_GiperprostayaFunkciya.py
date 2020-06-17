n = int(input())

def isPrime(n):
    k = 2
    while k * k <= n:
        if n % k == 0:
            return False
        k += 1
    return True

def isHyperPrime(n):
    while n > 0:
        if not isPrime(n):
            return False
        n //= 10
    return True

if isHyperPrime(n):
    print("YES")
else:
    print("NO")