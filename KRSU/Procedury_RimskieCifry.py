n = int(input())
#I -1, V – 5, X – 10, L – 50, C – 100, D – 500, M – 1000
def printyara(x, v, i, k):
    if k < 4:
        for j in range(0, k):
            print(i, end = "")
    elif k == 4:
        print(i, end = "")
        print(v, end = "")
    elif k == 9:
        print(i, end = "")
        print(x, end = "")
    else:
        print(v, end = "")
        for j in range(0, k - 5):
            print(i, end = "")

def rimskieCifry(n):
    for i in range(0, n // 1000):
        print("M", end = "")
    n %= 1000
    printyara("M", "D", "C", n // 100)
    n %= 100
    printyara("C", "L", "X", n // 10)
    n %= 10
    printyara("X", "V", "I", n)

rimskieCifry(n)