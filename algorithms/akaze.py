import itertools

import cv2
import numpy as np


def scaled_size(image_shape: tuple, scale_percent: int) -> tuple:
    width = int(image_shape[1] * scale_percent / 100)
    height = int(image_shape[0] * scale_percent / 100)

    return width, height


def filter_image(image):
    # Get HSV image from original one
    hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    # Filter white color
    white_sensitivity = 50
    white_lower_threshold = np.array([0, 0, 255])
    white_higher_threshold = np.array([255, white_sensitivity, 255])
    white_mask = cv2.inRange(hsv_image, white_lower_threshold, white_higher_threshold)

    # Filter blue color
    blue_sensitivity = 20
    blue_lower_threshold = np.array([110, blue_sensitivity, blue_sensitivity])
    blue_higher_threshold = np.array([130, 128, 255])
    blue_mask = cv2.inRange(hsv_image, blue_lower_threshold, blue_higher_threshold)

    # Conjunct two masks
    mask = cv2.bitwise_or(white_mask, blue_mask)

    # Apply masks on original image
    image = cv2.bitwise_and(image, image, mask=mask)
    return image


def check(logo_path: str, image_path: str, debug: bool) -> bool:
    # Load logo and inverse its colors
    logo = cv2.imread(logo_path)
    resized_logo = cv2.resize(logo, scaled_size(logo.shape, 25), interpolation=cv2.INTER_CUBIC)
    logo = resized_logo
    logos = [cv2.bitwise_not(resized_logo), resized_logo]

    # Load image, filter and upscale
    image = cv2.imread(image_path)
    size_scales = [scaled_size(image.shape, int(((x * logo.shape[1]) / image.shape[1]) * 100))
                   for x in [16, 14, 12, 10, 8, 6, 2]]
    if debug:
        print(size_scales)
        print("{:-^40}".format('-'))

    filtered_image = filter_image(image)
    images = [
        [cv2.cvtColor(cv2.resize(image, size_scale), cv2.COLOR_BGR2GRAY),
         cv2.cvtColor(cv2.resize(filtered_image, size_scale), cv2.COLOR_BGR2GRAY)] for size_scale in size_scales]
    images = list(np.array(images, dtype=object).flat)

    # Initialize the AKAZE descriptor
    detector = cv2.AKAZE_create()
    # Initialize FLANN matcher
    FLANN_INDEX_LSH = 6
    index_params = dict(algorithm=FLANN_INDEX_LSH,
                        table_number=12,
                        key_size=20,
                        multi_probe_level=2)
    search_params = dict()
    matcher = cv2.FlannBasedMatcher(index_params, search_params)

    min_matches = 8  # The minimal amount of matches to be certain
    nn_match_ratio = 0.625  # Ratio of good distance

    for current_logo, current_image in itertools.product(logos, images):
        (keypoints_logo, descriptors_logo) = detector.detectAndCompute(current_logo, None)
        (keypoints_image, descriptors_image) = detector.detectAndCompute(current_image, None)

        # Match the features
        matches = matcher.knnMatch(descriptors_logo, descriptors_image, k=2)

        if len(matches) < min_matches:
            continue

        # Get good matches
        good = []
        matches = [match for match in matches if len(match) == 2]
        for m, n in matches:
            if m.distance < nn_match_ratio * n.distance:
                good.append([m])

        if debug:
            print("Logo:\nkeypoints: {}, descriptors: {}".format(len(keypoints_logo), descriptors_logo.shape))
            print("{:-^40}".format('-'))
            print("Image:\nkeypoints: {}, descriptors: {}".format(len(keypoints_image), descriptors_image.shape))
            print("{:-^40}".format('-'))

            print("Matches total: {}, good matches: {}".format(len(matches), len(good)))
            print("{:-^40}".format('-'))

            result = cv2.drawMatchesKnn(current_logo, keypoints_logo, current_image,
                                        keypoints_image, good, None, flags=2)
            cv2.imshow("AKAZE matching", cv2.resize(result, scaled_size(result.shape, 10)))
            cv2.waitKey(0)

        if len(good) >= min_matches:
            return True

    return False
