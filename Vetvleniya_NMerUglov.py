n = int(input())
a = list(map(int, input().split()))
sush = True
sum = 0

for i in a:
    sum += i
    if i > 180 or i <= 0:
        sush = False

print(sum)

if sush:
    print("YES")
else:
    print("NO")