import cv2

def show_any(title, img: dict|cv2.Mat | None):
    if isinstance(img, cv2.Mat):
        show_image(title, img)
        
    elif isinstance(img, dict):
        show_images(title, img)
            
    else:
        print("Error: Invalid image type")



def show_image(title: str, img: cv2.Mat | None):
    try:
        cv2.imshow(title, img)
        cv2.waitKey(0)

    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        cv2.destroyAllWindows()


def show_images(images_dict: dict):
    try:
        for title, image in images_dict.items():
            cv2.imshow(title, image)

        cv2.waitKey(0)
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        cv2.destroyAllWindows()