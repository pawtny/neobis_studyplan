n = int(input())

def dvoich(n):
    s = ""
    while n:
        s += "-"
        n -= 1
    print(s)

dvoich(n)