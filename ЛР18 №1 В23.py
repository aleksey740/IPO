from PIL import Image
# Открываем изображение
image = Image.open('doroga.jpg')
# Отображаем изображение с использованием внешней программы по умолчанию
image.show()
# Сохраняем изображение
image.save('image1_23.png')
# Выводим характеристики изображения
print(f'Размер: {image.size}')
print(f'Формат: {image.format}')
print(f'Цветовой формат: {image.mode}')
