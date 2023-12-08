#Определяем список.
numbers = [1, 2, 3, 4, 5]
#Инициализируем переменные для суммы и произведениz.
sum_of_numbers = 0
pro_of_numbers = 1
#Проходим по каждому элементу списка.
for num in numbers:
    #Считаем сумму
    sum_of_numbers += num
    #Считаем произведение.
    pro_of_numbers *= num
#Выводим сумму и произведение.
print("Сумма элементов списка:", sum_of_numbers)
print("Произведение элементов списка:", pro_of_numbers)
