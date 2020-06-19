a, b = map(int, input().split())

sieve = [0] * 100001
sieve[0] = sieve[1] = 1

for i in range(2, 100001):
    if sieve[i] == 0:
        for j in range (i + i, 100001, i):
            sieve[j] = 1

boo = True

for i in range(a + 1, b):
    if sieve[i] == 0:
        if not boo:
            print(" ", end = "")
        print(i, end = "")
        boo = False