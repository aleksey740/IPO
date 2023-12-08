import math
a = 3/4
b = 1.11
y = [(math.sqrt(a/(b+math.cos(0.45-a)**2))) for x in range(3)] + [4.45/(b-(math.log(a)/a**math.cos(b)))]
print(y[0])
