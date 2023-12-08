def is_equilateral_triangle(a, b, c):
    if a == b and b == c:
        return True
    else:
        return False
a = float(input("Введите длину стороны a: "))
b = float(input("Введите длину стороны b: "))
c = float(input("Введите длину стороны c: "))
if is_equilateral_triangle(a, b, c):
    print("Треугольник равносторонний.")
else:
    print("Треугольник не равносторонний.")
