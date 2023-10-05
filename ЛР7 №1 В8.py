#Создаем список из семи городов.
city = ["Ошмяны", "Вильнюс", "Островец", "Гродно", "Минск", "Сморгонь", "Варшава"]
#Преобразуем список в кортеж.
city_tuple = tuple(city)
#Создаем новый кортеж new_tu из первых трех элементов кортежа cities_tuple.
new_tu = city_tuple[0:3]
#Создаем новый кортеж new_tu2 из четырех оставшихся элементов кортежа cities_tuple.
new_tu2 = city_tuple[3:]
#Создаем кортеж all_tu который содержит все созданные кортежи.
all_tu = (city_tuple, new_tu, new_tu2)
#Выводим результаты.
print(city_tuple)
print(new_tu)
print(new_tu2)
print(all_tu)
