from functools import cmp_to_key
class U:
    def __init__(self, id, score):
        self.id = id
        self.score = score
    
    def __repr__(self):
        return "{} {}".format(self.id, self.score)
    
    def comparator(self, b):
        if self.score == b.score:
            return -1 if self.id < b.id else 1
        return -1 if self.score > b.score else 1
n = int(input())
a = []

for i in range(n):
    x, y = map(int, input().split())
    a.append (U(x, y))

a.sort(key = cmp_to_key(U.comparator))
for i in a:
    print(i)
