n = int(input())

def dvoich(n):
    s = ""
    k = 128
    while k > 0:
        s += str(n // k)
        n %= k
        k //= 2
    return s

print(dvoich(n))