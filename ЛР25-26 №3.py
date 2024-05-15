import numpy as np

#Создание массива размером 3x4 с числами из нормального распределения
array_3x4 = np.random.normal(loc=0, scale=1.0, size=(3, 4))
print("Исходный двумерный массив:")
print(array_3x4)

#Преобразование массива в одномерный массив с сохранением атрибута size
array_1d = array_3x4.ravel()
print("\nПреобразованный одномерный массив:")
print(array_1d)
print("Атрибут size исходного массива:", array_3x4.size)
print("Атрибут size преобразованного массива:", array_1d.size)
