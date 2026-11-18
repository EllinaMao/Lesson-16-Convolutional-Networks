# Підготуйте фотографію текстового документа до розпізнавання. 
# Необхідно перетворити кольорове зображення на відтінки сірого та підібрати порогове значення threshold так, щоб максимально відокремити темний текст від світлого фону, 
# після чого зберегти підготовлений сканований варіант.

import cv2
import os
from helpers.save import save_images
from helpers.resize_if_large import resize_if_large
from helpers.show import show_images

from helpers.get_image_path import get_image_path

if __name__ == "__main__":
    image = get_image_path("./assets/txt_doc.jpg")
    image_resized = resize_if_large(image.copy(), 1000)


    gray = cv2.cvtColor(image_resized, cv2.COLOR_BGR2GRAY)

    threshold_value, binary = cv2.threshold(
        gray,
        165, 
        255,
        cv2.THRESH_BINARY
    )

    result = {
        'Colors_txt_doc Original Image': image_resized,
        'Gray txt_doc Image': gray,
        'Binary txt_doc Image': binary,
    }

    show_images(result)

    if not os.path.exists('code_results'):
        os.makedirs('code_results')

    save_images(result, 'code_results')

