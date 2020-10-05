import cv2
import sys
import cv2
import imutils
import numpy as np
import matplotlib.pyplot as plt


def check(logo_path: str, image_path: str) -> bool:
    logo = cv2.imread(logo_path)
    logo = cv2.resize(logo, (0, 0), fx=0.4, fy=0.4)

    image = cv2.imread(image_path)

    h, w,m = image.shape

    if h > 1000:
        image = cv2.resize(image, (0, 0), fx=0.7, fy=0.7)
    grey_logo = cv2.cvtColor(logo, cv2.COLOR_BGR2GRAY)
    grey_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    _, mask = cv2.threshold(grey_image, 220, 220, cv2.THRESH_BINARY_INV)
    _, mask_l = cv2.threshold(grey_logo, 230, 255, cv2.THRESH_BINARY_INV)

    #mask_l = cv2.Canny(mask_l, 689, 1322)
    canny_image = cv2.Canny(mask, 689, 1322)
    (tH, tW) = canny_image.shape[:2]


    while True:
        mask_l = cv2.resize(mask_l, (0, 0), fx=0.95, fy=0.95)

        res = cv2.matchTemplate(mask, mask_l, cv2.TM_SQDIFF)
        plt.imshow(res, cmap='gray')

        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)

        top_left = min_loc  # Change to max_loc for all except for TM_SQDIFF
        height, width = mask_l.shape[::]

        bottom_right = (top_left[0] + width, top_left[1] + height)
        newImage = mask.copy()
        cv2.rectangle(newImage, top_left, bottom_right, (255, 0,0 ), 2)

        cv2.imshow("Matched image", newImage)
        cv2.imshow('fff',mask_l)
        cv2.waitKey()
        cv2.destroyAllWindows()
        h, w = mask_l.shape

        if h < 150:
            break
    return


    canny_image = cv2.Canny(mask, 689, 1322)
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
    cv2.imshow('Matchs', mask)

    cv2.waitKey()

    return False
