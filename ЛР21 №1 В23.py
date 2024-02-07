import requests  #Импорт модуля для отправки HTTP-запросов
from bs4 import BeautifulSoup  #Импорт модуля для парсинга HTML
import csv  #Импорт модуля для работы с CSV-файлами

url = "https://bnb.by/kursy-valyut/imbank/"  #URL веб-страницы с курсами валют
user_agent = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.84 Safari/537.36 OPR/85.0.4341.72'}
#Заголовки HTTP-запроса, чтобы веб-сайт думал, что запрос приходит от браузера
r = requests.get(url, headers=user_agent)  #Отправка GET-запроса к веб-странице
print(r)
soup = BeautifulSoup(r.text, "html.parser")  #Создание объекта BeautifulSoup для парсинга HTML

items = soup.find_all("tr")  #Поиск всех элементов <tr> (строк) на веб-странице
items.pop(0)  #Удаление первой строки, так как это заголовок таблицы

curr = []  #Создание списка для хранения данных о курсах валют

for item in items:  #Итерация по найденным строкам таблицы
    temp = item.find_all("td")  #Поиск всех элементов <td> (ячеек) в текущей строке
    curr.append({
        'Валюта': temp[0].get_text(strip=True),  #Извлечение текста из первой ячейки (без лишних пробелов)
        'Покупка': temp[1].get_text(strip=True).replace('.', ','),  #Извлечение текста из второй ячейки, замена точек на запятые
        'Продажа': temp[2].get_text(strip=True).replace('.', ',')  #Извлечение текста из третьей ячейки, замена точек на запятые
    })


with open('curr_bank.csv', "w") as file:
    writer = csv.DictWriter(
        file,
        fieldnames=['Валюта', 'Покупка', 'Продажа'],  #Указание заголовков для CSV-файла
        delimiter=';',  #Установка разделителя полей в CSV-файле
        lineterminator='\r',  #Установка символа завершения строки в CSV-файле
        quoting=csv.QUOTE_MINIMAL  #Установка минимальных правил квотирования
    )
    writer.writeheader()  #Запись заголовка в CSV-файл
    for elem in curr:  #Итерация по данным и запись их в CSV-файл
        writer.writerow(elem)

print('Запись окончена')  #Вывод сообщения об успешном завершении программы
