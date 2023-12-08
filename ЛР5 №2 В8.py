def replace_z_with_mean(array): #array - это модуль который определяет  массивы.
    #Создаем список элементов.
    no_z_elements = [num for num in array if num != 0]
    #Вычисляем среднее арифметическое элементов.
    m = sum(no_z_elements) / len(no_z_elements) if no_z_elements else 0
    #Заменяем нулевые элементы на среднее арифметическое.
    replaced_array = [m if num == 0 else num for num in array]

    return replaced_array

array = [1, 2, 0, 4, 0, 6]
print("Исходный массив:", array)
array_with_mean_replaced = replace_z_with_mean(array)
print("Массив с замененными нулями:", array_with_mean_replaced)
