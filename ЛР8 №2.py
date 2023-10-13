#ввод элементов
set1 = set(map(int, input("Введите элементы первого множества через пробел: ").split()))
set2 = set(map(int, input("Введите элементы второго множества через пробел: ").split()))
#нахождение все различных числа в этих множествах
numbers_set1 = set1
numbers_set2 = set2
#нахождние числа которые входят в оба множества.sorted используется для сортировки элементов
common_numbers = sorted(list(numbers_set1.intersection(numbers_set2)))
#Вывод
print("Уникальные числа в первом множестве:", numbers_set1)
print("Уникальные числа во втором множестве:", numbers_set2)
print("Числа, входящие в оба множества в порядке возрастания:", common_numbers)
