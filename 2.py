import cv2
import numpy as np

cap =  cv2.imread("kd1.jpg")

template = cv2.imread("33.jpg", cv2.IMREAD_GRAYSCALE)
template1 = cv2.imread("44.jpg", cv2.IMREAD_GRAYSCALE)
template2 = cv2.imread("55.jpg", cv2.IMREAD_GRAYSCALE)
template3 = cv2.imread("66.jpg", cv2.IMREAD_GRAYSCALE)

'_____'
w3, h3 = template3.shape[::-1]
gray_frame3 = cv2.cvtColor(cap,cv2.COLOR_BGR2GRAY)

res3 = cv2.matchTemplate(gray_frame3, template3, cv2.TM_CCOEFF_NORMED)
loc3 = np.where(res3 >= 0.7)
    
for pt in zip(*loc3[::-1]):
    cv2.rectangle(cap, pt, (pt[0] + w3, pt[1] + h3), (0, 0, 255), 3)
'_____'
w2, h2 = template2.shape[::-1]
gray_frame2 = cv2.cvtColor(cap,cv2.COLOR_BGR2GRAY)

res2 = cv2.matchTemplate(gray_frame2, template2, cv2.TM_CCOEFF_NORMED)
loc2 = np.where(res2 >= 0.7)
    
for pt in zip(*loc2[::-1]):
    cv2.rectangle(cap, pt, (pt[0] + w2, pt[1] + h2), (0, 0, 255), 3)
'_____'
w1, h1 = template1.shape[::-1]
gray_frame1 = cv2.cvtColor(cap,cv2.COLOR_BGR2GRAY)

res1 = cv2.matchTemplate(gray_frame1, template1, cv2.TM_CCOEFF_NORMED)
loc1 = np.where(res1 >= 0.7)
    
for pt in zip(*loc1[::-1]):
    cv2.rectangle(cap, pt, (pt[0] + w1, pt[1] + h1), (0, 0, 255), 3)
'_____'
w, h = template.shape[::-1]
gray_frame = cv2.cvtColor(cap,cv2.COLOR_BGR2GRAY)

res = cv2.matchTemplate(gray_frame, template, cv2.TM_CCOEFF_NORMED)
loc = np.where(res >= 0.7)
    
for pt in zip(*loc[::-1]):
    cv2.rectangle(cap, pt, (pt[0] + w, pt[1] + h), (0, 255, 0), 3)
'_____'

cv2.imshow('yyy'+'.jpg',cap)

key = cv2.waitKey()

cv2.destroyAllWindows()
