import os

def check_image_requirements(image, title):
    height, width = image.shape[:2]
    if image.shape[2] != 3:
        print(f"Error: Image '{title}' does not have 3 channels.")
        return False
    if width < 800 or height < 600:
        print(f"Error: Image '{title}' resolution is less than 800x600.") 
        return False
    if not os.path.exists('processed'):
        os.makedirs('processed')

    return True
