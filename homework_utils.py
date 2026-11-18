# Створіть утиліту для перевірки відповідності зображення технічним вимогам. Програма має перевіряти, чи зображення має 3 канали та чи його роздільна здатність не менша за 800х600. Якщо умови виконано, збережіть його у папку processed, інакше виведіть помилку в консоль.
import os
from helpers.save import save_image
from helpers.show import show_image
from helpers.resize_if_large import resize_if_large
from helpers.get_image_path import get_image_path
from helpers.check_requirements import check_image_requirements

def check_and_save_image(image, title):
    if check_image_requirements(image, title):
        save_image(img = image, path = f'processed/{title}.jpg')
        show_image(title, image)
    else:
        print("Image does not meet the requirements.")

if __name__ == "__main__":
    #wrong image path for testing
    image = get_image_path("./assets/cyberpunk.jpg")
    wrong = resize_if_large(image, 1000)

    check_and_save_image(wrong, 'Wrong Image')
    check_and_save_image(image, 'Correct Image')