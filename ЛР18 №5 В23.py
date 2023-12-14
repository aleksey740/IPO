from PIL import Image, ImageDraw, ImageFont
# Открываем изображение
image = Image.open('image1_23.png')
# Создаем объект для рисования на изображении
draw = ImageDraw.Draw(image)
# Указываем координаты для левого нижнего угла и правого верхнего угла прямоугольника
rectangle_coordinates = (10, image.size[1] - 30, 180, image.size[1])
# Рисуем прямоугольник с белым цветом на заднем плане
draw.rectangle(rectangle_coordinates, fill='white')
# Указываем путь к файлу ttf-шрифта Arial
font_path = "arial.ttf"
# Создаем объект шрифта
font = ImageFont.truetype(font_path, size=14)
# Указываем координаты для размещения текста внутри прямоугольника
text_coordinates = (20, image.size[1] - 25)
# Пишем текст "Сакович" внутри прямоугольника
draw.text(text_coordinates, "Сакович", font=font, fill='black')
# Сохраняем изображение под новым именем
image.save('image1_23_2.png')
# Выводим характеристики сохраненного изображения
print(f'Размер: {image.size}')
print(f'Формат: {image.format}')
print(f'Цветовой формат: {image.mode}')