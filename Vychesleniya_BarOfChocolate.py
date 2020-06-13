a, b = map(int, input().split())
mult = min(a, b)
breaks = (max(a, b) - 1) * mult + mult - 1
print(breaks)