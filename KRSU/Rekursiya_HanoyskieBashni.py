n = int(input())

def hanoy(a, b, c, n):
    if n == 1:
        print(a, "->", c)
        return 1
    sum = hanoy(a, c, b, n - 1) + 1
    print(a, "->", c)
    return sum + hanoy(b, a, c, n - 1)

print(hanoy(1, 2, 3, n))