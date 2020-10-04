import cv2
import sys
import cv2
import numpy as np
import matplotlib.pyplot as plt


def check(logo_path: str, image_path: str) -> bool:
    logo = cv2.imread(logo_path)
    image = cv2.imread(image_path)

    _, mask = cv2.threshold(image, 230, 255, cv2.THRESH_BINARY_INV)

    # Creating a 3x3 kernel
    kernel = np.ones((3, 3), np.uint8)
    # Performing dilation on the mask
    dilation = cv2.dilate(mask, kernel)

    # Plotting the images
    titles = ["image", "mask", "dilation"]
    images = [image, mask, dilation]

    for i in range(3):
        plt.subplot(1, 3, i + 1), plt.imshow(images[i], "gray")
        plt.title(titles[i])
        plt.xticks([]), plt.yticks([])
    plt.show()

    grey_logo = cv2.cvtColor(logo, cv2.COLOR_BGR2GRAY)
    grey_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    canny_image = cv2.Canny(grey_image, 689, 1322)
    (tH, tW) = canny_image.shape[:2]

    canny_logo = cv2.Canny(grey_logo, 689, 1322)
    (tH, tW) = canny_logo.shape[:2]

    orb = cv2.ORB_create()
    kp1, des1 = orb.detectAndCompute(mask, None)
    kp2, des2 = orb.detectAndCompute(canny_logo, None)

    # matcher takes normType, which is set to cv2.NORM_L2 for SIFT and SURF, cv2.NORM_HAMMING for ORB, FAST and BRIEF
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)
    matches = bf.match(des1, des2)
    matches = sorted(matches, key=lambda x: x.distance)

    match_img = cv2.drawMatches(canny_image, kp1, canny_logo, kp2, matches, None)
    cv2.imshow('Matches', match_img)

    cv2.waitKey()

    return False
