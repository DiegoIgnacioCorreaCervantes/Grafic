import cv2 as cv
import numpy as np

# Leer la imagen en formato RGB
imagen = cv.imread('salida.png', 1)

hsv = cv.cvtColor(imagen, cv.COLOR_BGR2HSV)
uba=(10, 255, 255)
ubb=(0, 40 ,40)
uba2=(180, 255, 255)
ubb2=(170, 40,40)
mask1 = cv.inRange(hsv, ubb, uba)
mask2 = cv.inRange(hsv, ubb2, uba2)
mask = mask1+mask2
#res = cv.bitwise_and(imagen, imagen, mask=mask)
x,y = mask.shape

for i in range(x):
    for j in range(y):
        if(mask[i,j]==0):
            mask[i,j]=150
        else:
            mask1[i,j]=180
        cv.imshow('salida', mask)
        cv.waitKey(0)


cv.imshow('mask1', mask1)
#cv.imshow('res', res)
#cv.imshow('hsv', hsv )

cv.waitKey(0)
cv.destroyAllWindows()