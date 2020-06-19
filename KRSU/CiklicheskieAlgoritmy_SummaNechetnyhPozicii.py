n = int(input())
l = len(str(n))
sum = 0

for i in range(1, l + 1):
    if i % 2 != 0:
        sum += n // (10 ** (l - i))
    n %= 10 ** (l - i)

print(sum)