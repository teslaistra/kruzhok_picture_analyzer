import cv2


def check(logo_path: str, image_path: str) -> bool:
    logo = cv2.imread(logo_path)
    image = cv2.imread(image_path)

    grey_logo = cv2.cvtColor(logo, cv2.COLOR_BGR2GRAY)
    grey_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    return False
