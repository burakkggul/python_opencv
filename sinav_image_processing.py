import cv2
import numpy as np
import imutils

image = cv2.imread("image/picasso.jpg")
cv2.imshow("Orginal",image)
#cv2.waitKey(0)

#İmage Translation

M = np.float32([[1,0,25],[0,1,50]]) #Burda translation matrix'i oluşturuyoruz.

shifted = cv2.warpAffine(image,M,(image.shape[1],image.shape[0])) # Asıl kaydırma burada yapılıyor.

cv2.imshow("Shifted Right and Down",shifted)
#cv2.waitKey(0)

#Image Translation imutils

shifted = imutils.translate(image,25,50)
cv2.imshow("Imutils Shifted Right and Down",shifted)
#cv2.waitKey(0)

#Rotation

(h,w) = image.shape[:2]
center = ((image.shape[1]//2),(image.shape[0]//2))

M = cv2.getRotationMatrix2D(center,45,1.0) #Burada döndürme matrix'ini oluşturduk
rotated = cv2.warpAffine(image,M,(w,h)) #Burada ise döndürme işlemini gerçekleştirdik
cv2.imshow("Rotated",rotated)
#cv2.waitKey(0)

#Rotation Imutils

rotated = imutils.rotate(image,45)
cv2.imshow("Rotated Imutils",rotated)
#cv2.waitKey(0)

#Resize

r = 150.0 / image.shape[1]
dim = (150,int(image.shape[0]*r))
resized = cv2.resize(image,dim,interpolation = cv2.INTER_AREA)
cv2.imshow("Resized Width",resized)
cv2.waitKey(0)

#Flipping

flipped = cv2.flip(image,1)

cv2.imshow("Flipping",flipped)
#cv2.waitKey(0)

#Cropping

cropped = image[30:120,40:130]
cv2.imshow("Cropped",cropped)
#cv2.waitKey(0)

#Image Arithmetic

#cv2 ile toplama işlemi

print("max of 255 : {}".format(cv2.add(np.uint8([200]),np.uint8([100])))) #255'den yüksekse 255 alınıyor düşükse 0 alınıyor.
print("min of 0 : {}".format(cv2.subtract(np.uint8([50]),np.uint8([100]))))

#Numpy ile toplama işlemi

print("Wrap around : {}".format(np.uint8([200])+np.uint8([100]))) #Mod 256 alınıyor.
print("Wrap around : {}".format(np.uint8([50])-np.uint8([100])))

#Image Arithmetic Resim Soluklaştırma

M = np.ones(image.shape,image.dtype) *100

added = cv2.add(image,M)
cv2.imshow("White Matris",M)
cv2.imshow("Added",added)
#cv2.waitKey(0)

M = np.ones(image.shape,image.dtype) *50
subtracted = cv2.subtract(image,M)
cv2.imshow("Subtracted",subtracted)
#cv2.waitKey(0)

rectangle = np.zeros((300,300),dtype = "uint8")
cv2.rectangle(rectangle,(25,25),(275,275),255,-1)
cv2.imshow("Rectangle",rectangle)
cv2.waitKey(0)

circle = np.zeros((300,300),dtype = "uint8")
cv2.circle(circle,(150,150),150,255,-1)
cv2.imshow("Circle",circle)
cv2.waitKey(0)

bitwiseAnd=cv2.bitwise_and(circle,rectangle)
cv2.imshow("Bitwise And",bitwiseAnd)
cv2.waitKey(0)

#Masking

mask = np.zeros(image.shape[:2],dtype = "uint8")
(cX,cY) = ((image.shape[1]//2),(image.shape[0]//2))
cv2.rectangle(mask,(cX-75,cY-75),(cX+75,cY+75),255,-1)
cv2.imshow("Mask",mask)
masked = cv2.bitwise_and(image,image,mask = mask)
cv2.imshow("Mask applied Image",masked)
cv2.waitKey(0)

#Splitting and Merging Channel

(B,G,R) = cv2.split(image)
cv2.imshow("Red",R)
cv2.imshow("Green",G)
cv2.imshow("Blue",B)
cv2.waitKey(0)

merged = cv2.merge([B,G,R])
cv2.imshow("Merged",merged)
cv2.waitKey(0)

zeros = np.zeros(image.shape[:2],image.dtype)
cv2.imshow("Red",cv2.merge([zeros,zeros,R]))
cv2.imshow("Green",cv2.merge([zeros,G,zeros]))
cv2.imshow("Blue",cv2.merge([B,zeros,zeros]))
cv2.waitKey(0)

#Color Spaces

gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
hsv = cv2.cvtColor(image,cv2.COLOR_BGR2HSV)
lab = cv2.cvtColor(image,cv2.COLOR_BGR2LAB)
cv2.imshow("Gray",gray)
cv2.imshow("hsv",hsv)
cv2.imshow("lab",lab)
cv2.waitKey(0)


