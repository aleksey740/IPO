import requests

link = "https://browser-info.ru/"
responce = requests.get(link).text

with open("1.html", "w", encoding="utf-8") as file:
    file.write(responce)