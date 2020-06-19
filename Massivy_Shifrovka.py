s = input()
n = len(s) // 2 if len(s) % 2 == 0 else len(s) // 2 + 1
a = [0] * len(s)
c = 0

for i in range(n):
    a[c] = s[i]
    c += 2

c = 1

for i in range(n, len(s)):
    a[c] = s[i]
    c += 2

c = 0

for i in range(len(s)):
        if a[i] == s[i]:
            c += 1

print(c)