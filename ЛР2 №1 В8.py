import math as m

a = 2.7
b = -3.59

x = int(input("Введите x: "))
if x > 2:
    y = (m.cos(a * x)**2)**3
elif x > 6:
    y = (m.sin(x)**2)**2 + b / x
else:
    y = (2 - x**2)**3
print("y =", y)

