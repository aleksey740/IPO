from PIL import Image
# Открываем изображение
image = Image.open('image2_23.png')
# Определяем координаты обрезки левый верхний угол и правый нижний угол
crop_coordinates = (100, 50, 800, 600)
# Обрезаем изображение
cropped_image = image.crop(crop_coordinates)
# Сохраняем полученное обрезанное изображение
cropped_image.save('image3_23.png')
# Выводим характеристики изображения
print(f'Размер: {cropped_image.size}')
print(f'Формат: {cropped_image.format}')
print(f'Цветовой формат: {cropped_image.mode}')