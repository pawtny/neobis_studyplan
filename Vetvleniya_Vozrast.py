# -*- coding:cp1251 -*-
v = input()
r = int(v) % 10

if len(v) > 1 and v[len(v) - 2] == "1":
    print(u"Вам", v, u"лет.")
elif r == 0 or (5 <= r and r <= 9):
    print(u"Вам", v, u"лет.")
elif r == 1:
    print(u"Вам", v, u"год.")
else:
    print(u"Вам", v, u"года.")
