a, b = map(int, input().split())

for i in range (a, b + 1):
    print("{}*{}={}".format(i, i, i * i))