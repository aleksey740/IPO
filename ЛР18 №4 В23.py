from PIL import Image, ImageFilter
# Открываем изображение
image_nn = Image.open('image3_NN.png')
# Применяем фильтр контур к изображению и сохраняем результат
filtered_image_nn = image_nn.filter(ImageFilter.CONTOUR)
filtered_image_nn.save('image4_NN.png')
# Выводим характеристики сохраненного изображения
print(f'Размер: {filtered_image_nn.size}')
print(f'Формат: {filtered_image_nn.format}')
print(f'Цветовой формат: {filtered_image_nn.mode}')
# Открываем изображение 'image3_23.png'
image_23 = Image.open('image3_23.png')
# Применяем несколько фильтров размытие и увеличение резкости к изображению и сохраняем результат
filtered_image_23 = image_23.filter(ImageFilter.BLUR).filter(ImageFilter.SHARPEN)
filtered_image_23.save('image4_23.png')
# Выводим характеристики сохраненного изображения
print(f'Размер: {filtered_image_23.size}')
print(f'Формат: {filtered_image_23.format}')
print(f'Цветовой формат: {filtered_image_23.mode}')