import cv2

image = cv2.imread("image/picasso.jpg")
cv2.imshow("Original",image)
cv2.waitKey(0)


flipped = cv2.flip(image,1)
cv2.imshow("Flipped Horizontally",flipped)
cv2.waitKey(0)

flipped = cv2.flip(image,0)
cv2.imshow("Flipped Vertically",flipped)
cv2.waitKey(0)

flipped = cv2.flip(image,-1)
cv2.imshow("Flipped Horizontally & Vertically",flipped)
cv2.waitKey(0)