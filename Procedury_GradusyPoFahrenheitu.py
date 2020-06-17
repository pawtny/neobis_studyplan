import math
n = int(input())

def toFahrenheit(n):
    return math.floor(n * 1.8 + 32)

print(toFahrenheit(n))