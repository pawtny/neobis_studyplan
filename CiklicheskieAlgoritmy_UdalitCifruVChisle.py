s = input()
x = input()
s = s.replace(x, "")
if s == "" or int(s) == 0:
    print()
else:
    print(int(s))