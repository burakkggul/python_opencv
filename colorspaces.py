import cv2
import numpy as np

image = cv2.imread("image/picasso.jpg")
cv2.imshow("Orginal",image)
cv2.waitKey(0)

gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
cv2.imshow("Gray",gray)
cv2.waitKey(0)

hsv = cv2.cvtColor(image,cv2.COLOR_BGR2HSV)
cv2.imshow("HSV",hsv)
cv2.waitKey(0)

lab = cv2.cvtColor(image,cv2.COLOR_BGR2LAB)
cv2.imshow("LAB",lab)
cv2.waitKey(0)
cv2.destroyAllWindows()