import glob

import cv2
import numpy as np


def check(logo_path: str, image_path: str, debug: bool) -> bool:
    template_path = "".join([logo_path, "*.jpg"])
    template_files = glob.glob(template_path)
    templates = [cv2.imread(f, cv2.IMREAD_GRAYSCALE) for f in template_files]

    if not templates:
        return False

    if debug:
        print(f"Found {len(templates)} templates to use")

    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

    locale_ratio = 0.7
    rectangle_color = (0, 0, 255)

    features = []
    for template in templates:
        try:
            width, height = template.shape[::-1]
            match_result = cv2.matchTemplate(image, template, cv2.TM_CCOEFF_NORMED)
            locale_features = np.where(match_result >= locale_ratio)
            for point in zip(*locale_features[::-1]):
                cv2.rectangle(image, point, (point[0] + width, point[1] + height), color=rectangle_color, thickness=3)

            if len(locale_features) > 0:
                features.append(locale_features)

        except Exception as e:
            if debug:
                print(e)
            continue

        if debug:
            print(f"Added {len(features)} new local features")
            cv2.imshow('result' + '.jpg', image)
            cv2.waitKey()

    return len(features) >= 1
