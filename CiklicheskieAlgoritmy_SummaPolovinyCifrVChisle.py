a = input()
n = int(a)

def summa(k):
    sum = 0
    while k > 0:
        sum += k % 10
        k //= 10
    return int(sum)

if len(a) % 2 == 0:
    print(summa(n // (10 ** (len(a) / 2))))
else:
    print(summa(n))