import numpy as np
import cv2

image = cv2.imread("image/picasso.jpg")
cv2.imshow("Original",image)
cv2.waitKey(0)

print("max of 255 : {}".format(cv2.add(np.uint8([200]),(np.uint8([100])))))
print("min of 0 : {}".format(cv2.subtract(np.uint8([50]),(np.uint8([100])))))

print("wrap around : {}".format(np.uint8([200])+np.uint8([100])))
print("wrap around : {}".format(np.uint8([50])-np.uint8([100])))

M = np.ones(image.shape,image.dtype)*100

added = cv2.add(image,M)

cv2.imshow("Added",added)
cv2.waitKey(0)

M = np.ones(image.shape,image.dtype)*50
subtracted = cv2.subtract(image,M)
cv2.imshow("Subtracted",subtracted)
cv2.waitKey(0)
