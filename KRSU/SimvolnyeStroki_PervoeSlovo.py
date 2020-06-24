n = input().strip()
if n.find(" ") == -1:
    print(n)
else:
    print(n[0 : n.find(" ")])
