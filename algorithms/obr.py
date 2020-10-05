import cv2
import matplotlib.pyplot as plt


def check(logo_path: str, image_path: str, debug: bool) -> bool:
    # подгружаем лого, и целевое изображение
    # масштабируя его под адекватный размер для удобного вывода
    logo = cv2.imread(logo_path)
    logo = cv2.resize(logo, (0, 0), fx=0.4, fy=0.4)

    image = cv2.imread(image_path)

    # размеры целевого изображения
    h, w, m = image.shape

    # масштабируем изображение в случае его
    # слишком высокого размера для удобного вывода
    if h > 1000:
        image = cv2.resize(image, (0, 0), fx=0.7, fy=0.7)

    # Получаем версии картинок с серым фильтром
    grey_logo = cv2.cvtColor(logo, cv2.COLOR_BGR2GRAY)
    grey_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Накидываем маску, которая дает самый эффективный эффект отсеивания лишних объектов помимо лого
    # TODO: тесты различных значений threshold'а с помощью ползунков на UI для подбора оптимального
    _, mask = cv2.threshold(grey_image, 220, 220, cv2.THRESH_BINARY_INV)
    _, mask_l = cv2.threshold(grey_logo, 230, 255, cv2.THRESH_BINARY_INV)

    # mask_l = cv2.Canny(mask_l, 689, 1322)
    # канни-маска для изображения
    # mask_l = cv2.Canny(mask_l, 689, 1322)
    canny_image = cv2.Canny(mask, 689, 1322)
    (tH, tW) = canny_image.shape[:2]

    # прогоняем поиск логотипа, уменьшая его каждую итерацию
    while True:
        mask_l = cv2.resize(mask_l, (0, 0), fx=0.95, fy=0.95)

        # сравниваем лого и картинку
        res = cv2.matchTemplate(mask, mask_l, cv2.TM_SQDIFF)
        plt.imshow(res, cmap='gray')

        # далее считаем где отрисовать квадрат
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)

        top_left = min_loc  # Change to max_loc for all except for TM_SQDIFF
        height, width = mask_l.shape[::]
        if width > 0:
            return True
        bottom_right = (top_left[0] + width, top_left[1] + height)
        newImage = mask.copy()
        cv2.rectangle(newImage, top_left, bottom_right, (255, 0, 0), 2)

        if debug:
            cv2.imshow("Matched image", newImage)
            cv2.imshow('fff', mask_l)
            cv2.waitKey()
            cv2.destroyAllWindows()

        h, w = mask_l.shape

        # если лого совсем крошечный, то уходим
        if h < 150:
            return False

    # далее идет кусок кода, который соотносит лого и изображение посредством фич на ORB-алгоритме
    # работает плохо - нужно увеличивать размер фич
    # для того чтоб не путать прямые линии логотипа и любых других на самом изображении
    # TODO: разобраться как увеличить размер фич для повышения корректности нахождения
    # накладывем canny-фильтр на изображение и лого, лучше использовать на цветном изображении
    canny_image = cv2.Canny(mask, 689, 1322)
    (tH, tW) = canny_image.shape[:2]

    canny_logo = cv2.Canny(grey_logo, 689, 1322)
    (tH, tW) = canny_logo.shape[:2]

    # применяем orb-алгоритм к изображениям, для нахождения фич
    orb = cv2.ORB_create()
    kp1, des1 = orb.detectAndCompute(mask, None)
    kp2, des2 = orb.detectAndCompute(canny_logo, None)

    # Соотносим фичи, и сортируем их по дистанциям
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)
    matches = bf.match(des1, des2)
    matches = sorted(matches, key=lambda x: x.distance)

    # выводим соотнесенные фичи
    match_img = cv2.drawMatches(canny_image, kp1, canny_logo, kp2, matches, None)
    cv2.imshow('Matches', match_img)
    cv2.imshow('Matchs', mask)

    cv2.waitKey()
    if debug:
        match_img = cv2.drawMatches(canny_image, kp1, canny_logo, kp2, matches, None)
        cv2.imshow('Matches', match_img)
        cv2.imshow('Matchs', mask)
        cv2.waitKey()

    return False
