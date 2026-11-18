import cv2

def get_image_path(path = './assets/cyberpunk.jpg'):
    image = cv2.imread(path)

    if image is None:
        raise ValueError(f"Unable to load image at {path}")

    return image

  