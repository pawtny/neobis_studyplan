n = int(input())
k = n
def summacifr(n):
    sum = 0
    while n > 0:
        sum += n % 10
        n //= 10
    return sum

print(k % 10, end = "")
k //= 10
while k > 0:
        print("+{}".format(k % 10), end = "")
        k //= 10
else:
    print("={}".format(summacifr(n)))