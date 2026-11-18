def crop_center_square(image):
    height, width = image.shape[:2]
    min_dim = min(height, width)
    start_x = (width - min_dim) // 2
    start_y = (height - min_dim) // 2
    return image[start_y:start_y + min_dim, start_x:start_x + min_dim]
