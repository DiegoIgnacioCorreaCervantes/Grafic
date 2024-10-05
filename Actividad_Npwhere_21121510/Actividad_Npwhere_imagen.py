#Npwhere
import cv2
import numpy as np

# Leer la imagen en formato RGB
imagen = cv2.imread('f1.jpg', 1)

# Convertir la imagen de RGB a HSV
imagen_hsv = cv2.cvtColor(imagen, cv2.COLOR_BGR2HSV)

# Definir el rango de color rojo en HSV
bajo_rojo1 = np.array([0, 40, 40])
alto_rojo1 = np.array([10, 255, 255])
bajo_rojo2 = np.array([160, 40, 40])
alto_rojo2 = np.array([180, 255, 255])

# Definir el rango de color amarillo en HSV
bajo_amarillo = np.array([25, 40, 40])
alto_amarillo = np.array([30, 255, 255])

# Definir el rango de color verde en HSV
bajo_verde = np.array([32, 40, 40])
alto_verde = np.array([70, 255, 255])

# Definir el rango de color cian en HSV
bajo_cian = np.array([75, 40, 40])
alto_cian = np.array([95, 255, 255])

# Definir el rango de color magenta en HSV
bajo_magenta = np.array([145, 40, 40])
alto_magenta = np.array([155, 255, 255])

# Crear una máscara para el color rojo
mascara_rojo1 = cv2.inRange(imagen_hsv, bajo_rojo1, alto_rojo1)
mascara_rojo2 = cv2.inRange(imagen_hsv, bajo_rojo2, alto_rojo2)
mascara_rojo = cv2.add(mascara_rojo1, mascara_rojo2)

# Crear una máscara para el amarillo
mascara_amarillo = cv2.inRange(imagen_hsv, bajo_amarillo, alto_amarillo)

# Crear una máscara para el verde
mascara_verde = cv2.inRange(imagen_hsv, bajo_verde, alto_verde)

# Crear una máscara para el cian
mascara_cian = cv2.inRange(imagen_hsv, bajo_cian, alto_cian)

# Crear una máscara para el magenta
mascara_magenta = cv2.inRange(imagen_hsv, bajo_magenta, alto_magenta)

# Convertir la imagen original a escala de grises
imagen_gris = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)

# Convertir la imagen gris a un formato BGR para que coincida con la original
imagen_gris_bgr = cv2.cvtColor(imagen_gris, cv2.COLOR_GRAY2BGR)

# Combinar la imagen en gris con las áreas en rojo
img_rojo = np.where(mascara_rojo[:, :, None] == 255, imagen, imagen_gris_bgr)

# Combinar la imagen en gris con las áreas en amarillo
img_amarillo = np.where(mascara_amarillo[:, :, None] == 255, imagen, imagen_gris_bgr)

# Combinar la imagen en gris con las áreas en amarillo
img_verde = np.where(mascara_verde[:, :, None] == 255, imagen, imagen_gris_bgr)

# Combinar la imagen en gris con las áreas en amarillo
img_cian = np.where(mascara_cian[:, :, None] == 255, imagen, imagen_gris_bgr)

# Combinar la imagen en gris con las áreas en amarillo
img_magenta = np.where(mascara_magenta[:, :, None] == 255, imagen, imagen_gris_bgr)

# Mostrar la imagen final
cv2.imshow('Rojo', img_rojo)
cv2.imshow('Amarillo', img_amarillo)
cv2.imshow('Verde', img_verde)
cv2.imshow('Cian', img_cian)
cv2.imshow('Magenta', img_magenta)
cv2.imshow('imagen original', imagen)

cv2.waitKey(0)
cv2.destroyAllWindows()