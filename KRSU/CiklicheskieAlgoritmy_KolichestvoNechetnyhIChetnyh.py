n = int(input())
nechet = 0
chet = 0

while n > 0:
    if n % 10 % 2 == 0:
        chet += 1
    else:
        nechet += 1
    n //= 10

print(nechet, chet)