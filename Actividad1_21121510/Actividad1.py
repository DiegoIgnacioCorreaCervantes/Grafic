import cv2 as cv
import numpy as np
import math

img = cv.imread('gato.jpg', 0)
x, y = img.shape

#Crear una imagen vacia para almacenar el resultado
rotated_img = np.zeros((x*2, y*2), dtype = np.uint8)
xx, yy = rotated_img.shape
#Calcular el centro de la imagen
cx, cy = int(y // 2),int(x // 2) 
#Definir el angulo de rotacion en grados y convertirlo a radianes
angle = 60 
theta = math.radians(angle)

traslated_img = np.zeros((x,y), dtype=np.uint8)
for i in range(x):
    for j in range(y):
        #Trasladar
        traslated_img[int(i*0.5)+10,int(j*0.5)+10] = img[i,j]
        #Rotar
        new_x = int((j - cx) * math.cos(theta) - (i - cy) * math.sin(theta) + cx)
        new_y = int((j - cx) * math.sin(theta) + (i - cy) * math.cos(theta) + cy)
        if 0 <= new_x < y and 0 <= new_y < x:
            rotated_img[new_y, new_x] = img[i,j]

#Definir el factor de escala
scale_x, scale_y =0.2, 0.2

#Crear una nueva imagen para almacenar el escalado
scaled_img = np.zeros((int(x * scale_y), int(y * scale_x)), dtype=np.uint8)

#Aplicar el escalado
for i in range(int(x * scale_y)):
    for j in range(int(y * scale_x)):
        orig_x = int(i * scale_y)
        orig_y = int(j * scale_x)
        if 0 <= orig_x < x and 0 <= orig_y < y:
            scaled_img[i, j] = img[orig_x, orig_y]

cv.imshow('imagen normal', img)
cv.imshow('imagen trasladada', traslated_img)
cv.imshow('imagen rotada (modo raw)', rotated_img)
cv.imshow('Imagen Escalada (modo raw)', scaled_img)
cv.waitKey()
cv.destroyWindow