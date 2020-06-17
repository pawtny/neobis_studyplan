n = int(input())

if n < 0:
    print("ERROR")
elif n >= 2:
    sum = 0
    a = [0, 1, 1]
    while a[-1] < n:
        sum += a[-1]
        a.append(a[-1] + a[-2])
    print(sum)
else:
    print(n)
        