import numpy as np
def split_array(arr):
    #Используем маскирование для отделения положительных и отрицательных элементов
    positive_mask = arr > 0  #Создаем маску для положительных элементов
    negative_mask = arr < 0  #Создаем маску для отрицательных элементов

    #Используем маски для выбора элементов из исходного массива
    positive_arr = arr[positive_mask]  #Выбираем положительые элементы
    negative_arr = arr[negative_mask]  #выбираем отрицательные элементы

    return positive_arr, negative_arr  #Возвращаем новые массивы

#Пример использования функции:
original_array = np.array([1, -2, 3, -4, 5])  #Создаем исходный массив
positive_array, negative_array = split_array(original_array)  #Разделяем массив
print("Массив с положительными элементами:", positive_array) #Вывод массива
print("Массив с отрицательными элементами:", negative_array) #Вывод массива
