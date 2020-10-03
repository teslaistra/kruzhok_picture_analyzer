import cv2 as cv


def check(logo_path: str, image_path: str) -> bool:
    logo = cv.imread(cv.samples.findFile(logo_path), cv.IMREAD_GRAYSCALE)
    image = cv.imread(cv.samples.findFile(image_path), cv.IMREAD_GRAYSCALE)
    return False
