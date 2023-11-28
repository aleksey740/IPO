import random  #Импортируем модуль random для генерации случайных списков
import time  #Импортируем модуль time для измерения времени выполнения функции
from functools import wraps  #Импортируем wraps из functools для корректного копирования метаданных функций

#Декоратор для измерения времени выполнения функции
def timeit(method):
    @wraps(method)
    def timed(*args, **kw):
        ts = time.monotonic()  #Засекаем текущее время до выполнения функции
        result = method(*args, **kw)  #Вызываем целевую функцию
        te = time.monotonic()  #Засекаем текущее время после выполнения функции
        ms = (te - ts) * 1000  #Вычисляем время выполнения в миллисекундах
        all_args = ', '.join(tuple(f'{a!r}' for a in args) + tuple(f'{k}={v!r}' for k, v in kw.items()))
        #Форматируем аргументы функции для вывода
        print(f'{method.__name__}({all_args}): {ms:2.2f} ms')  # Выводим результат измерения времени
        return result
    return timed

#Функция сортировки пузырьком с использованием декоратора для измерения времени
@timeit
def bubble_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

#Проверка времени выполнения для разных размеров списка
for size in [10, 100, 1000, 10000, 100000]:
    random_list = random.sample(range(size * 10), size)  # Генерируем случайный список заданного размера
    bubble_sort(random_list.copy())  # Вызываем сортировку пузырьком для копии списка, чтобы не изменять оригинальный список
