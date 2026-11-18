import cv2


def resize_if_large(image, max_size=1800):
    if image is None:
        raise ValueError("Invalid image provided")
    
    img_h, img_w = image.shape[:2]
    
    max_side = max(img_w, img_h)
    
    if max_side <= max_size:
        return image
    
    scale = max_size / max_side
    new_w = int(img_w * scale)
    new_h = int(img_h * scale)
    
    return cv2.resize(image, (new_w, new_h), interpolation=cv2.INTER_AREA)