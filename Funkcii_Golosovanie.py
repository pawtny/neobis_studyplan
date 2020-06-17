n = int(input())

def golos(a, b, c):
    if a + b + c > 1:
        return True
    else:
        return False

while n:
    a, b, c = map(int, input().split())

    if golos(a, b, c):
        print(1)
    else:
        print(0)
    n -= 1