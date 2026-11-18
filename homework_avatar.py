# Напишіть скрипт для створення аватарки: програма має взяти зображення, вирізати з нього строго центральний квадрат, зменшити його розмір до 250х250 пікселів та повернути у правильну орієнтацію, якщо фото зроблене боком.


import cv2
import os
from helpers.save import save_image
from helpers.show import show_image

from helpers.get_image_path import get_image_path
from helpers.crop_center_square import crop_center_square


if __name__ == "__main__":
    image = get_image_path("./assets/cyberpunk.jpg")

    avatar = crop_center_square(image)
    avatar = cv2.resize(avatar, (250, 250))

    

    show_image('Avatar', avatar)

    if not os.path.exists('processed'):
        os.makedirs('processed')

    save_image(img = avatar, path ='code_results/avatar.jpg')
