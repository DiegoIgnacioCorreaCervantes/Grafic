import cv2 as cv
import numpy as np

# Cargar la imagen en escala de grises
img = cv.imread('f1.jpg', 0)

# Obtener el tamaño de la imagen
x, y = img.shape

# Definir el factor de escala
scale_x, scale_y = 2, 2

# Crear una nueva imagen para almacenar el escalado
scaled_img = np.zeros((int(x * scale_y), int(y * scale_x)), dtype=np.uint8)

# Aplicar el escalado
for i in range(x):
    for j in range(y):
        #orig_x = int(i * scale_y)
        #orig_y = int(j * scale_x)
        #if 0 <= orig_x < x and 0 <= orig_y < y:
            scaled_img[i*2, j*2] = img[i, j]
         

# Aplicar matriz 1/9
for i in range(x):
    for j in range(y):
        k = 0
        k = k + scaled_img[i-1][j-1]*(1/9)
        k = k + scaled_img[i][j-1]*(1/9)
        k = k + scaled_img[i+1][j-1]*(1/9)
        k = k + scaled_img[i-1][j]*(1/9)
        k = k + scaled_img[i][j]*(1/9)
        k = k + scaled_img[i+1][j]*(1/9)
        k = k + scaled_img[i-1][j+1]*(1/9)
        k = k + scaled_img[i][j+1]*(1/9)
        k = k + scaled_img[i+1][j+1]*(1/9)
        scaled_img[i][j] = k                 
        

# Mostrar la imagen original y la escalada
cv.imshow('Imagen Original', img)
cv.imshow('Imagen Escalada (modo raw)', scaled_img)
cv.waitKey(0)
cv.destroyAllWindows()