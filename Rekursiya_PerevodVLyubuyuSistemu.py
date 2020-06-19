n, k = map(int, input().split())

def convert(n, k):
    bible = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    if n < k:
        return bible[n]
    return convert(n // k, k) + bible[n % k]

print(convert(n, k))