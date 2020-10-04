import cv2
import numpy as np

cap =  cv2.imread("1.bmp")
template = cv2.imread("111.jpg", cv2.IMREAD_GRAYSCALE)
w, h = template.shape[::-1]
gray_frame = cv2.cvtColor(cap,cv2.COLOR_BGR2GRAY)

res = cv2.matchTemplate(gray_frame, template, cv2.TM_CCOEFF_NORMED)
loc = np.where(res >= 0.7)
    
for pt in zip(*loc[::-1]):
    cv2.rectangle(cap, pt, (pt[0] + w, pt[1] + h), (0, 255, 0), 3)

cv2.imwrite('yyy'+'.jpg',cap)

key = cv2.waitKey(1)

cv2.destroyAllWindows()
