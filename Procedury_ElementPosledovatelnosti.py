n = int(input())

def element(k):
    posled = [0] * 150
    posled[0] = 1
    posled[1] = 2
    posled[2] = 3
    for i in range(3, 150):
        posled[i] = posled[i - 1] + posled[i - 2] - 2 * posled[i - 3]
    return posled[k - 1]

print(element(n))