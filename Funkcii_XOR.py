n = int(input())

def xor(a, b):
    if a != b:
        return True
    return False

while n:
    a, b = map(int, input().split())

    if xor(a, b):
        print(1)
    else:
        print(0)
    n -= 1