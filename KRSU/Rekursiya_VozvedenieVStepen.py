a, b = map(int, input().split())

def pow(a, b):
    if b == 0:
        print(1)
        return 1

    print("%d*" % a, end = "")
    return pow(a, b - 1) * a

print(pow(a, b))