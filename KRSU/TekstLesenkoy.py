r = input()
a = r.split()
s = ""
for i in range(0, len(a)):
    print(s + a[i])
    for j in range(0, len(a[i])):
        s = s + " "