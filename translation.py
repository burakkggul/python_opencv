import numpy as np
import imutils
import cv2
import argparse



image = cv2.imread("image/picasso.jpg")
cv2.imshow("Original",image)
cv2.waitKey(0)

M = np.float32([[1,0,25],[0,1,50]])
shifted = cv2.warpAffine(image,M,(image.shape[1],image.shape[0]))
cv2.imshow("Shifted Down and Right",shifted)
cv2.waitKey(0)

M = np.float32([[1,0,-50],[0,1,-90]])
shifted = cv2.warpAffine(image,M,(image.shape[1],image.shape[0]))
cv2.imshow("Shifted Up and Left",shifted)
cv2.waitKey(0)

shifted = imutils.translate(image,0,100)
cv2.imshow("Shifted Down",shifted)  #İmutils kütüphanesi normalde numpy ile yapacağımız işlemi çok daha kısaltıyor.
cv2.waitKey()


