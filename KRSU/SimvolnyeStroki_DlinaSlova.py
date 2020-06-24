l = list(input().split())
maxi = 0

for i in range(len(l)):
    if len(l[i]) > len(l[maxi]):
        maxi = i

print(l[maxi])
print(len(l[maxi]))