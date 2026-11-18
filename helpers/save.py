
import cv2
import numpy as np
import os

def save_image(path: str, img: np.ndarray | None):
    try:
        if img is None or img.size == 0:
            raise ValueError("Image is empty")
            
        folder = os.path.dirname(path)
        if folder:
            os.makedirs(folder, exist_ok=True)
            
        success = cv2.imwrite(path, img)
        if not success:
            print(f"Failed to save image to {path}")
            
    except Exception as e:
        print(f"An error occurred while saving {path}: {e}")


def save_images(result: dict[str, np.ndarray], folder: str):
    for title, image in result.items():
        path = f"{folder}/{title.replace(' ', '_')}.png"
        save_image(path, image)