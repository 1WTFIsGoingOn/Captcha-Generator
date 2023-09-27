from PIL import Image
import random

def generate(captcha = 'Random'):
    if captcha == 'Random':
        s = '2345679ACEFHKLMNPRTUVXYZ'
        captcha = ''.join(random.sample(s, 4))
    width, height = 104, 29

    #Склейка букв
    result_image = Image.new("RGB", (width, height))
    i = 0
    for char in captcha:
        letter = Image.open(f"letters\{char}.png")

        result_image.paste(letter, (i, 0))
        i += 26

    # Проходим по каждому пикселю изображения
    for x in range(width):
        for y in range(height):
            # Получаем цвет текущего пикселя
            pixel = result_image.getpixel((x, y))

            # Если пиксель чёрный, заменяем его на случайный сине-зелёный оттенок
            if pixel == (0, 0, 0):
                random_color = (0, random.randint(0, 255), random.randint(0, 255))
                result_image.putpixel((x, y), random_color)
    
    # Интенсивность шума - количество точек для добавления
    intensity = 150

    for _ in range(intensity):
        x = random.randint(0, width-1)
        y = random.randint(0, height-1)
        noise = (0, random.randint(100, 255), random.randint(100, 255))  # Сине-зелёный оттенок
        result_image.putpixel((x, y), noise)

    # Сохраняем изменённое изображение
    output_image_path = f"process/{captcha}.png"
    result_image.save(output_image_path)
    print(f'Captcha {captcha} сгенерирована!')
    return captcha


if __name__ == "__main__":
    captcha = input('Сгенерировать определённую капчу? Y/N: ').upper()
    if captcha == 'Y':
        print('Доступные символы: 2345679ACEFHKLMNPRTUVXYZ')
        captcha = input('Введите капчу, которую нужно сгенерировать: ').upper()
        response = generate(captcha)
    elif captcha == 'N':
        loops = input('Введите количество: ')
        for i in range(int(loops)):
            generate()

    input('Нажмите любую клавишу для выхода...')
    
