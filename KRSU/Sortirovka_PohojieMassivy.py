n = int(input())
a = list(map(int, input().split()))
m = int(input())
b = list(map(int, input().split()))

a.sort()
b.sort()

i = 0
j = 0
boo = True
while i < len(a) or j < len(b):
    if(a[i] != b[j]):
        boo = False
        break
    while i < len(a) - 1 and a[i] == a[i + 1]:
        i += 1
    while j < len(b) - 1 and b[j] == b[j + 1]:
        j += 1
    i += 1
    j += 1

print("YES") if boo else print("NO")