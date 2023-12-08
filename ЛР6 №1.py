temperatures_info = [
    [-8, -14, -19, -18],#температура 1-й метеостанции
    [25, 28, 26, 20], #температура 2-й метеостанции
    [11, 18, 20, 25]] #температура 3-й метеостанции
#Диапазон температур
minimal_temperature = 24
maximal_temperature = 26
#enumerate — это функция которая используется для добавления счетчика к списку, кортежу, строке.
for stations_num, temperatures in enumerate(temperatures_info, start=1):
    print(f"Данные для метеостанции {stations_num}:")
    for day_number, temperature in enumerate(temperatures, start=1):
        #Проверяем диапазон температуры.
        if minimal_temperature <= temperature <= maximal_temperature:
            print(f"На {day_number}-й день температура была {temperature} градусов")
