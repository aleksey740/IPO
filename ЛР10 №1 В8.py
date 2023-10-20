#Запрос количества чисел
N = int(input("Введите количество чисел: "))
#Запрос целых чисел и запись в файл
with open(f'file1_08.txt', 'w') as f1:
    for i in range(N):
        num = int(input(f"Введите целое число {i+1}: "))
        f1.write(str(num) + '\n')
#Чтение чисел из файла и вычисление среднего геометрического нечетных чисел
odd_numbers = []
with open(f'file1_08.txt', 'r') as f1:
    numbers = f1.readlines()
    for num in numbers:
        num = int(num)
        if num % 2 != 0:
            odd_numbers.append(num)
#Вычисление среднего геометрического
if odd_numbers:
    geometric_mean = 1
    for num in odd_numbers:
        geometric_mean *= num
    geometric_mean = geometric_mean ** (1 / len(odd_numbers))
else:
    geometric_mean = 0
#Запись среднего геометрического в файл
with open(f'file2_08.txt', 'w') as f2:
    f2.write(f"Среднее геометрическое нечетных чисел: {geometric_mean}")

