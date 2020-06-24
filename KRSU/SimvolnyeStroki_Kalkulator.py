def meh(a, b, op):
    if op == "+":
        return int(a) + int(b)
    if op == "-":
        return int(a) - int(b)
    if op == "*":
        return int(a) * int(b)
    if op == "/":
        return int(a) // int(b)


n = input()
l = [0] * 5
i = 0
j = 0
while True:
    if not n[i].isdigit():
        l[j] = n[0: i] 
        j += 1
        l[j] = n[i]
        n = n[i + 1:]
        i = -1
        j += 1
        if j == 4:
            l[j] = n
            break
    i += 1

if l[1] == "-":
    l[1] = "+"
    l[2] = "-" + l[2]

if l[1] == "+":
    print(meh(l[0], meh(l[2], l[4], l[3]), l[1]))
else:
    print(meh(meh(l[0], l[2], l[1]), l[4], l[3]))