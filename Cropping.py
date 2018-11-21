import cv2

image = cv2.imread("image/picasso.jpg")
cv2.imshow("Original",image)
cv2.waitKey(0)

cropped = image[30:120,240:335]
cv2.imshow("Cropped",cropped)
cv2.waitKey(0)