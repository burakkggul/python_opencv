import cv2

image = cv2.imread("image/picasso.jpg")

print("width: {} pixels".format(image.shape[1]))
print("height: {} pixels".format(image.shape[0]))
print("channels: {} pixels".format(image.shape[2]))
cv2.namedWindow("Picasso",cv2.WINDOW_NORMAL)
cv2.imshow("Picasso",image)

(b,g,r) = image [0,0]
print ("pixel at (0,0) -Red: {} , Green : {}, Blue : {}".format(r,g,b))

image [0,0] = (0,0,255)
(b,g,r) = image[0,0]
print ("Pixel at (0,0) -Red : {},Green:{},Blue:{}".format(r,g,b))
cv2.waitKey(0)
cv2.destroyAllWindows()