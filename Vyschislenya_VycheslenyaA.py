x, y, z = [int(x) for x in input().split()] 
sum = "{}+{}+{}={}"
mul = "{}*{}*{}={}"
avr = "({}+{}+{})/3={}"
avrg = (x + y + z) / 3
print(sum.format(x, y, z, x + y + z))
print(mul.format(x, y, z, x * y * z))
if avrg - int(avrg) == 0:
    print(avr.format(x, y, z, int(avrg)))
elif int(avrg) < 10 and int(avrg) > -10:
    print(avr.format(x, y, z, format(avrg, ".5f")))
else:
    print(avr.format(x, y, z, format(avrg, ".4f")))