a, b, c = map(int, input().split())

def perestanovka(a, b , c):
    sum = a + b + c
    print(min(a, min(b, c)), sum - min(a, min(b, c)) - max(a, max(b, c)), max(a, max(b, c)))

perestanovka(a, b, c)