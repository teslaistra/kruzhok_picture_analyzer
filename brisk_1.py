import cv2
import numpy as np

def save_keypoints(image_path, type_image):
    img = cv2.imread(image_path)
    krug = cv2.imread("krug.bmp")
    krug1 = cv2.cvtColor(krug,cv2.COLOR_BGR2GRAY)
    img1= cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    kp, descriptors =cv2.BRISK_create(100).detectAndCompute(img1,krug1)
    mg=cv2.drawKeypoints(img1, kp, krug1, 
    flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
    cv2.imwrite('brisk_keypoints-'+ type_image+'.jpg',mg)

if __name__=="__main__":
    save_keypoints("2.bmp" ,"original")
