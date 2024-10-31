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

# Obtener el tamaño de la imagen escalada
xs, ys = scaled_img.shape

# Aplicar matriz de sobel
for i in range(xs):
    for j in range(ys):
        
        k = 0
        if (i-1)<0 or (j-1)<0:
            n=0
        else:
            n = int(scaled_img[i-1][j-1])
        k = k + n*(-1)
        if (j-1)<0:
             n=0
        else:
             n = int(scaled_img[i][j-1])
        k = k + n*(0)
        if (i+1)>=xs or (j-1)<0:
            n=0
        else:
            n = int(scaled_img[i+1][j-1])
        k = k + n*(1)
        if (i-1)<0:
            n=0
        else:   
            n = int(scaled_img[i-1][j])
        k = k + n*(-2)
       
        n = int(scaled_img[i][j])
        k = k + n*(0)

        if (i+1)>=xs:
            n = 0
        else:    
            n = int(scaled_img[i+1][j])
        k = k + n*(2)
        if (i-1)<0 or (j+1)>=ys:
            n=0
        else:
            n = int(scaled_img[i-1][j+1])
        k = k + n*(-1)
        if (j+1)>=ys:
            n=0
        else:
            n = int(scaled_img[i][j+1])
        k = k + n*(0)
        if (i+1)>=xs or (j+1)>=ys:
            n=0
        else:
            n = int(scaled_img[i+1][j+1])
        k = k + n*(1)

        if k > 255:
             k=255
        if k < 0:
             k=0

        scaled_img[i][j] = int(k)                 
        
# Mostrar la imagen original y la escalada
cv.imshow('Imagen Original', img)
cv.imshow('Imagen Escalada (modo raw)', scaled_img)
cv.waitKey(0)
cv.destroyAllWindows()