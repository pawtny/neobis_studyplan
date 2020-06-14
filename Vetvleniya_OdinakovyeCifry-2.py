a = input()
boo = False

for i in range(0, len(a)):
    for j in range(i + 1, len(a)):
        if a[i] == a[j]:
            boo = True

if boo:
    print("YES")
else:
    print("NO")