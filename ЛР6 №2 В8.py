def find_min_abs_index(arr):
    min_abs_value = float('inf')  #Переменную для хранения значения.
    min_abs_index = None  #Переменную для хранения индекса.

    for i in range(len(arr)):
        abs_value = abs(arr[i])  #Вычисляем модуль текущего элемента
        # Если модуль текущего элемента меньше минимального найденного значения, обновляем значения
        if abs_value < min_abs_value:
            min_abs_value = abs_value
            min_abs_index = i

    return min_abs_index
#Массив
arr = [5, -3, 8, -10, 4, 9, -2]
# Находим номер минимального по модулю элемента
min_abs_index = find_min_abs_index(arr)
# Выводим результат
if min_abs_index is not None:
    print("Номер минимального по модулю элемента:", min_abs_index)
    print("Значение минимального по модулю элемента:", arr[min_abs_index])
