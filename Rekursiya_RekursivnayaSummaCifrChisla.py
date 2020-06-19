n = int(input())

def summaCifr(n):
    if n < 10:
        print(n)
        return n
    print("%d+" % (n % 10), end = "")
    return n % 10 + summaCifr(n // 10)

print(summaCifr(n))