n = int(input())

def znakChisla(n):
    if n < 0:
        return -1
    if n > 0:
        return 1
    return 0

print(znakChisla(n))