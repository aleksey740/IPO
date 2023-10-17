#Функция для ввода массива
def input_array():
    m = int(input("Введите длину массива: "))  #Запрашиваем длину массива
    A = []  #Создание пустого массива
    for i in range(m):
        element = int(input(f"Введите элемент A[{i}]: "))  #Запрашиваем каждый элемент
        A.append(element)  #Добавляем элемент в массив
    return A
#Функция для замены первого и последнего элементов в массиве
def swap_elements(arr):
    if len(arr) >= 2:
        arr[0], arr[-1] = arr[-1], arr[0]
#Функция для вывода массива
def print_array(arr):
    for i, element in enumerate(arr):
        print(f"A[{i}] = {element}")
A = input_array()  #Вводим массив
print("Исходный массив:")
print_array(A)  #Вывод исходного массива
swap_elements(A)  #Меняем первый и последний элементы
print("Массив после замены:")
print_array(A)  #Вывод измененного массива
