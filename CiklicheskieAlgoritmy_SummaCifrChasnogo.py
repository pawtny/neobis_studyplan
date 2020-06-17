n = int(input())

print(1, end = "")
for i in range(2, n + 1):
    c = i
    boo = True
    while c > 0:
        v = c % 10
        if v == 0 or i % v != 0:
            boo = False
            break
        c //= 10
        
    if boo:
        print("", i, end = "")