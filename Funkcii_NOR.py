n = int(input())

def nor(a, b):
    return not(a or b)

while n:
    a, b = map(int, input().split())

    if nor(a, b):
        print(1)
    else:
        print(0)
    n -= 1