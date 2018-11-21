import cv2
import numpy as np

image = cv2.imread("image/picasso.jpg")
cv2.namedWindow("Orginal",cv2.WINDOW_NORMAL)
cv2.imshow("Orginal",image)
cv2.waitKey(0)

(b,g,r) = image[0,0] #noktasındaki pixel değerini ata
print("b:{} g:{} r:{}".format(b,g,r))
image[0,0] = (0,0,255) #Red rengi 0,0 pixeline ata
cv2.namedWindow("0,0 Red",cv2.WINDOW_NORMAL)
cv2.imshow("0,0 Red",image)
cv2.waitKey(0)

corner = image[0:100,0:100] #image'in 0:100 ve 0:100 pixellerini al
cv2.imshow("Corner",corner)
cv2.waitKey(0)

image[0:100,0:100] = (0,255,255)
cv2.imshow("Updated",corner)
cv2.waitKey(0)

canvas = np.zeros((300,300,3),dtype = "uint8")
cv2.imshow("Canvas",canvas)
cv2.waitKey(0)

cv2.line (canvas,(300,0),(0,300),255,3)
cv2.imshow("Canvas Line",canvas)
cv2.waitKey(0)

green = (0,255,0)
cv2.rectangle(canvas,(10,10),(60,60),green,-1)
cv2.imshow("Rectangle",canvas)
cv2.waitKey(0)

cv2.circle(canvas,(150,150),150,green,3)
cv2.imshow("Circle",canvas)
cv2.waitKey(0)

(centerX,centerY) = ((canvas.shape[1]//2),(canvas.shape[0]//2) )

for r in range (0,175,25):
    cv2.circle(canvas,(centerX,centerY),r,255,1)
cv2.imshow("Circle circle",canvas)
cv2.waitKey(0)

canvas = np.zeros((300,300,3),dtype = "uint8")

for i in range(0,25):
    radius = np.random.randint(5,high = 200)
    pt = np.random.randint(0,high = 300,size = (2,))
    color = np.random.randint(0,high = 256,size = (3,)).tolist()
    cv2.circle(canvas,tuple(pt),radius,color,1)
cv2.imshow("Random Circle",canvas)
cv2.waitKey(0)



