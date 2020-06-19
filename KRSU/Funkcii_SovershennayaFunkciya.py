n = int(input())

def isPerfect(n):
    if n % 2 != 0:
        return False
    sum = 0
    for i in range(1, n // 2 + 1):
        if n % i == 0:
            sum += i
    return sum == n

if isPerfect(n):
    print("YES")
else:
    print("NO")

#Time-limit exceeded