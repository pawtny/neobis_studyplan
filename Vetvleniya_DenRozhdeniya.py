d, m = map(int, input().split())
a = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
dni = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
n = 1

for i in range(0, m - 1):
    n += a[i]

n += d + 3 #2016 nachinaetsya s pyathicy
print(dni[n % 7 - 1])