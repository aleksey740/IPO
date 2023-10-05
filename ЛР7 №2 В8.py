#Создаем словарь с файлами и их размерами.
file_system = {
    "реферат.docx": 1024,  # Размер в байтах
    "image.jpeg": 2048,
    "video.mp4": 4096,
    "music.mp3": 512,
    "ЛР7 №2.py": 256,
    "index.html": 768,
    "python.exe": 1536,
}
#пары ключзначение; items() это метод который возвращает обьект который получает ключ
for file_name, size in file_system.items():
    print(f"Файл: {file_name}, Размер: {size} байт")
#Запрашиваем ключ для поиска значения.
key = input("Введите ключ для поиска значения: ")
#Ищем значение по ключу.
if key in file_system:
    print(f"Значение для ключа '{key}': {file_system[key]} байт")
else:
    print(f"Ключ '{key}' не найден в словаре.")
