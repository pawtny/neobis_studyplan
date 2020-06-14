a, b = map(int, input().split())
sum = 0

for i in range (0, abs(a)):
    sum += b

if a < 0 and b < 0:
    sum = -sum
    print("({})*({})={}".format(a, b, sum))
elif a < 0:
    sum = -sum
    print("({})*{}={}".format(a, b, sum))
elif b < 0:
    print("{}*({})={}".format(a, b, sum))
else:
    print("{}*{}={}".format(a, b, sum))