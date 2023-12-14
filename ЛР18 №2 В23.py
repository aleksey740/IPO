from PIL import Image
# Открываем изображение
image = Image.open('image1_23.png')
# Поворачиваем изображение на 20 градусов против часовой стрелки
rotated_image = image.rotate(-20)
# Сохраняем полученное изображение
rotated_image.save('image2_23.png')
# Выводим характеристики изображения
print(f'Размер: {rotated_image.size}')
print(f'Формат: {rotated_image.format}')
print(f'Цветовой формат: {rotated_image.mode}')
