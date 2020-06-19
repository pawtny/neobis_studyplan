s = input()


if int(s) % (10 ** (len(s) - 1)) // 10 != 0:
    print(int(s) % (10 ** (len(s) - 1)) // 10)
else:
    print()