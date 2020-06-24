n = input()
x = input()
indo = -1
for i in range(len(n) - 1, -1, -1):
    if n[i] == ".":
        indo = i
        break

if indo >= 0:
    print(n[0 : indo + 1] + x)
else:
    print(n + "." + x)