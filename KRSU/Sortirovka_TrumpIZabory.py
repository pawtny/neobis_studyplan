from functools import cmp_to_key
class U:
    def __init__(self, name, cena, kach):
        self.name = name
        self.cena = cena
        self.kach = kach
    
    def __repr__(self):
        return "{}".format(self.name)
    
    def comparator(self, b):
        if self.cena == b.cena:
            return 1 if self.kach < b.kach else -1
        return 1 if self.cena > b.cena else -1 
n = int(input())
a = []

for i in range(n):
    s, x, y = map(str, input().split())
    a.append (U(s, int(x), int(y)))

a.sort(key = cmp_to_key(U.comparator))
print(a[0])
