n = int(input())
a = list(map(int, input().split()))
sum = 0
boo = True

for i in a:
    sum += i

for i in a:
    if i >= sum - i:
        boo = False
        break

print("YES") if boo else print("NO")