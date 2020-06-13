n, a, d = map(int, input().split())
sumN = (2 * a + d * (n - 1)) / 2 * n
print(int(sumN / n))