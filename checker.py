import sys
import cv2

print(sys.argv[1:])

image = cv2.imread(sys.argv[1])

cv2.imshow("image",image)
cv2.waitKey(0)
cv2.destroyAllWindows()
