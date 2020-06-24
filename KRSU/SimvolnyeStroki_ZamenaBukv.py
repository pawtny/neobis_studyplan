a = input()
s = list(a)
for i in range(len(s)):
    if s[i] == "a":
        s[i] = "b"
    elif s[i] == "A":
        s[i] = "B"
    elif s[i] == "b":
        s[i] = "a"
    elif s[i] == "B":
        s[i] = "A"

print("".join(s))