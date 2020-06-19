n = int(input())

def cifry(n):
    length = 0
    k = n

    while k:
        k //= 10
        length += 1
    
    while length:
        print(n // (10 ** (length - 1)))
        n %= 10 ** (length - 1)
        length -= 1


cifry(n)