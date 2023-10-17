def is_divisible_digits(num):
    #Преобразование числа в строку
    num_str = str(num)
    #Перебор всех цифор в числе
    for digit in num_str:
        #Преобразование цифры в целое число
        digit_int = int(digit)
        #Проверяем, делится ли число на эту цифру без остатка
        if digit_int == 0 or num % digit_int != 0:
            return False
    #Если все цифры успешно без остатка, возвращаем True
    return True

def find_numbers(n):
    #Создание списка для хранения найденных чисел
    divisible_numbers = []
    #Перебор всех натуральных чисел от 1 до n
    for i in range(1, n + 1):
        #Проверяем, делится ли число на каждую свою цифру
        if is_divisible_digits(i):
            divisible_numbers.append(i)
    return divisible_numbers
#Заданный n
n = 100
#Вызов функции и вывод результата
result = find_numbers(n)
print(f'Натуральные числа,которые делятся на каждую из своих цифр не превосходящие заданного {n}:{result}')
