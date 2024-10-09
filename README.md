# Documentacion del repositorio 
---

## Unidad 1
---
### Dibujo pixel art
#### codigo:

~~~
import cv2 as cv
import numpy as np

img = np.ones((500,500), dtype=np.uint8) * 240

#Arriba izquierdo
img[30][30]=1
img[30][31]=1
img[30][32]=1
img[30][33]=1
img[30][34]=1
img[30][35]=1
img[30][36]=1
img[30][37]=1
img[30][38]=1
img[30][39]=1
img[30][40]=1
img[30][41]=1
img[30][42]=1
img[30][43]=1
img[30][44]=1
img[30][45]=1
img[30][46]=1
img[30][47]=1
img[30][48]=1
img[30][49]=1
img[30][50]=1
img[30][51]=1
img[31][51]=1
img[32][51]=1
img[33][51]=1
img[34][51]=1
img[35][51]=1

#centro corazon
img[36][52]=1
img[37][52]=1
img[37][53]=1
img[38][53]=1
img[38][54]=1
img[39][54]=1
img[40][55]=1
img[39][56]=1
img[38][56]=1
img[38][57]=1
img[37][57]=1
img[37][58]=1
img[36][58]=1

#Arriba derecho
img[30][59]=1
img[30][60]=1
img[30][61]=1
img[30][62]=1
img[30][63]=1
img[30][64]=1
img[30][65]=1
img[30][66]=1
img[30][67]=1
img[30][68]=1
img[30][69]=1
img[30][70]=1
img[30][71]=1
img[30][72]=1
img[30][73]=1
img[30][74]=1
img[30][75]=1
img[30][76]=1
img[30][77]=1
img[30][78]=1
img[30][79]=1
img[30][80]=1
img[30][58]=1
img[31][58]=1
img[32][58]=1
img[33][58]=1
img[34][58]=1
img[35][58]=1

#Lado izquierdo
img[31][30]=1
img[31][29]=1
img[32][29]=1
img[32][28]=1
img[33][28]=1
img[33][27]=1
img[34][27]=1
img[34][26]=1
img[35][26]=1
img[35][25]=1
img[36][25]=1
img[36][24]=1
img[37][24]=1
img[37][23]=1
img[38][23]=1
img[38][22]=1
img[39][22]=1
img[40][22]=1
img[41][22]=1
img[42][22]=1
img[43][22]=1
img[44][22]=1
img[45][22]=1
img[46][22]=1
img[47][22]=1
img[47][23]=1
img[48][23]=1
img[48][24]=1
img[49][24]=1
img[49][25]=1
img[50][25]=1
img[50][26]=1
img[51][26]=1
img[51][27]=1
img[52][28]=1
img[53][29]=1
img[54][30]=1
img[55][31]=1
img[56][32]=1
img[57][33]=1
img[58][34]=1
img[59][35]=1
img[60][36]=1
img[61][37]=1
img[62][38]=1
img[63][39]=1
img[64][40]=1
img[65][41]=1
img[66][42]=1
img[67][43]=1
img[68][44]=1
img[69][45]=1
img[70][46]=1
img[71][47]=1
img[72][48]=1
img[73][49]=1
img[74][50]=1
img[75][51]=1
img[76][52]=1

#punta corazon
img[77][52]=1
img[77][53]=1
img[78][53]=1
img[78][54]=1
img[79][55]=1
img[78][56]=1
img[78][57]=1
img[77][57]=1
img[77][58]=1

#Lado derecho
img[31][80]=1
img[31][81]=1
img[32][81]=1
img[32][82]=1
img[33][82]=1
img[33][83]=1
img[34][83]=1
img[34][84]=1
img[35][84]=1
img[35][85]=1
img[36][85]=1
img[36][86]=1
img[37][86]=1
img[37][87]=1
img[38][87]=1
img[38][88]=1
img[39][88]=1
img[40][88]=1
img[41][88]=1
img[42][88]=1
img[43][88]=1
img[44][88]=1
img[45][88]=1
img[46][88]=1
img[47][88]=1
img[47][87]=1
img[48][87]=1
img[48][86]=1
img[49][86]=1
img[49][85]=1
img[50][85]=1
img[50][84]=1
img[51][84]=1
img[51][83]=1
img[52][82]=1
img[53][81]=1
img[54][80]=1
img[55][79]=1
img[56][78]=1
img[57][77]=1
img[58][76]=1
img[59][75]=1
img[60][74]=1
img[61][73]=1
img[62][72]=1
img[63][71]=1
img[64][70]=1
img[65][69]=1
img[66][68]=1
img[67][67]=1
img[68][66]=1
img[69][65]=1
img[70][64]=1
img[71][63]=1
img[72][62]=1
img[73][61]=1
img[74][60]=1
img[75][59]=1
img[76][58]=1

cv.imshow('img', img)
cv.waitKey()
cv.destroyAllWindows()
~~~

<br>

![Ejecución](https://github.com/DiegoIgnacioCorreaCervantes/Grafic/blob/main/Imagenes_archivomd/pixelart_ejecucion.png)
</br>

---

### Transformaciones geometricas
#### codigo:
~~~
import cv2 as cv
import numpy as np
import math

img = cv.imread('gato.jpg', 0)
x, y = img.shape

traslated_img = np.zeros((x,y), dtype=np.uint8)
for i in range(x):
    for j in range(y):
        traslated_img[int(i*0.5)+60,int(j*0.5)+50] = img[i,j]

#Crear una imagen vacia para almacenar el resultado
rotated_img = np.zeros((x*2, y*2), dtype = np.uint8)
xx, yy = rotated_img.shape
#Calcular el centro de la imagen
cx, cy = int(y // 2),int(x // 2) 

#Definir el angulo de rotacion en grados y convertirlo a radianes
angle = 45 
theta = math.radians(angle)

#Rotar la imagen
for i in range(x):
    for j in range(y):
        new_x = int((j - cx) * math.cos(theta) - (i - cy) * math.sin(theta) + cx)
        new_y = int((j - cx) * math.sin(theta) + (i - cy) * math.cos(theta) + cy)
        if 0 <= new_x < y and 0 <= new_y < x:
            rotated_img[new_y, new_x] = img[i,j]

#Definir el factor de escala
scale_x, scale_y =0.8, 0.8

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
~~~

</br>

![Ejecución](https://github.com/DiegoIgnacioCorreaCervantes/Grafic/blob/main/Imagenes_archivomd/transformaciones_geometricas_ejecucion.png)
</br>

---

### Investigacion Ecuaciones parametricas

En matemáticas, un sistema de ecuaciones paramétricas permite representar una curva o superficie en el plano o en el espacio, mediante valores que recorren un intervalo de números reales, mediante una variable, llamada parámetro, considerando cada coordenada de un punto como una función dependiente del parámetro.

En el uso estándar del sistema de coordenadas, una o dos variables (dependiendo de si se utilizan dos o tres dimensiones respectivamente) son consideradas como variables independientes, mientras que la restante es la variable dependiente, con el valor de esta siendo equivalente al de la imagen de la función cuando los restantes valores son sus parámetros. Así por ejemplo la expresión de un punto cualquiera 
(x, y) equivale a la expresión (x, f(x)).

Esta representación tiene la limitación de requerir que la curva sea una función de x en y, es decir que todos los valores x tengan un solo valor y (y solamente uno) correspondiente en y. No todas las curvas cumplen con dicha condición. Para poder trabajar con la misma como si se tratara de una función, lo que se hace es elegir un dominio y una imagen diferentes, en donde la misma sí sea función. Para hacer esto, tanto x como y son considerados variables dependientes, cuyo resultado surge de una tercera variable (sin representación gráfica) conocida como «parámetro».

En algunos casos, ayuda a simplificar la derivación y la integración, en vez del caso y = f(x) o de z = F(x, y).

<br>

#### Ejemplo
Sea 3x-2y-5=0 la ecuación general de una recta, entonces caben las ecuaciones paramétricas:
<br>

![](https://github.com/DiegoIgnacioCorreaCervantes/Grafic/blob/main/Imagenes_archivomd/IP1.png)
<br>

#### Otro ejemplo
Dada la ecuación y=x^2 una parametrización tendrá la forma               
<br>                                                                               
![](https://github.com/DiegoIgnacioCorreaCervantes/Grafic/blob/main/Imagenes_archivomd/IP2.png)
<br>

Una parametrización posible sería 
<br>

![](https://github.com/DiegoIgnacioCorreaCervantes/Grafic/blob/main/Imagenes_archivomd/IP3.png)
<br>

Se debe destacar que para cada curva existen infinitas parametrizaciones posibles. Una en donde x e y equivaliesen a 2U y 4U^2 con U∈R, respectivamente, sería igualmente válida. La diferencia sería que, para encontrar un punto determinado (a, b) de la curva, el valor del parámetro sería diferente en cada caso. Con el ejemplo dado, el punto (2, 4) de la curva aparecería en la primera parametrización cuando t = 2, y en el segundo cuando U = 1.
<br>

#### Curvas
La expresión paramétrica de una función permite la construcción de una gran variedad de formas, simplemente variando alguna constante. A continuación, se describe la función paramétrica:
<br>

![](https://github.com/DiegoIgnacioCorreaCervantes/Grafic/blob/main/Imagenes_archivomd/IP4.png)
<br>

que, para la cual, dependiendo del ratio a/b pueden obtenerse formas muy diversas.

En esta otra función se puede ver una gran variedad de formas en función de los exponentes j y k, variando los parámetros a, b, c y d.
<br>

![](https://github.com/DiegoIgnacioCorreaCervantes/Grafic/blob/main/Imagenes_archivomd/IP5.png)

<br>

#### Diferentes figuras variando k:

![](https://github.com/DiegoIgnacioCorreaCervantes/Grafic/blob/main/Imagenes_archivomd/IP6.png)
<br>

---
<br>

### Dibujo usando primitivas de dibujo
#### Codigo:

~~~
import cv2 as cv
import numpy as np

img = np.ones((500, 500, 3), dtype=np.uint8)*255

cv.rectangle(img, (0,0), (500,270), (255,255,0), -1)
cv.circle(img, (250, 210), 90, (0,255,255), -1)
cv.rectangle(img, (0,270), (500,500), (0,182,141), -1)

cv.circle(img, (75, 55), 28, (255,255,255), -1)
cv.circle(img, (45, 60), 18, (255,255,255), -1)
cv.circle(img, (105, 60), 15, (255,255,255), -1)

cv.circle(img, (275, 65), 28, (255,255,255), -1)
cv.circle(img, (240, 70), 18, (255,255,255), -1)
cv.circle(img, (305, 70), 15, (255,255,255), -1)

cv.circle(img, (465, 35), 28, (255,255,255), -1)
cv.circle(img, (435, 40), 18, (255,255,255), -1)
cv.circle(img, (495, 40), 15, (255,255,255), -1)

cv.imshow('imagen', img)
cv.waitKey()
cv.destroyWindow()
~~~
<br>

![Ejecucion](https://github.com/DiegoIgnacioCorreaCervantes/Grafic/blob/main/Imagenes_archivomd/PDE.png)
<br>

---

### Dibujar 10 Parametricas
#### Codigo:

~~~
#Curva de Limacon
import cv2 as cv2
import numpy as np

# Definir los parámetros iniciales
width, height = 1000, 1000  # Ampliar la ventana para ver toda la figura
img = np.ones((height, width, 3), dtype=np.uint8)*255

# Parámetros de la curva de Limacon
a, b = 150, 100  # Reducir los valores de a y b para que la curva se ajuste mejor
k = 0.5 # Constante de multiplicación del ángulo
theta_increment = 0.05  # Incremento del ángulo
max_theta = 2 * np.pi  # Un ciclo completo

# Centro de la imagen
center_x, center_y = width // 2, height // 2

theta = 0  # Ángulo inicial

while True:  # Bucle infinito
    # Limpiar la imagen
    img = np.ones((width, height, 3), dtype=np.uint8) * 255
    
    # Dibujar la curva completa desde 0 hasta theta
    for t in np.arange(0, theta, theta_increment):
        # Calcular las coordenadas paramétricas (x, y) para la curva de Limacon
        #r = a + b * np.cos(k * t)
        r = a + b * np.cos(k * t)
        #x = int(center_x + r * np.cos(t))
        #y = int(center_y + r * np.sin(t))
        x = int(center_x + r * np.sin(t))
        y = int(center_y + r * np.cos(t))
        
        # Dibujar un círculo en la posición calculada
        cv2.circle(img, (x, y), 2, (0, 234, 0), 2)  # Color rojo
        cv2.circle(img, (x-2, y-2), 2, (0, 0, 0), 2)  # Color rojo

    # Mostrar la constante k en la imagen
    #cv2.putText(img, f"k = {k:.2f}", (20, 40), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
    
    # Mostrar la imagen
    cv2.imshow("Parametric Animation", img)
    
    # Incrementar el ángulo
    theta += theta_increment
    
    # Reiniciar theta si alcanza su valor máximo
    #if theta >= max_theta:
    #    theta = 0  # Reinicia la animación para que se repita

    # Pausar para ver la animación
    if cv2.waitKey(30) & 0xFF == 27:  # Esperar 30ms, salir con 'ESC'
        break

# Cerrar la ventana al finalizar
cv2.destroyAllWindows()
~~~
<br>

Cambiamos el valor k para obtener diferentes graficas
<br>

![1.-](https://github.com/DiegoIgnacioCorreaCervantes/Grafic/blob/main/Imagenes_archivomd/DP1.png)
<br>

![2.-](https://github.com/DiegoIgnacioCorreaCervantes/Grafic/blob/main/Imagenes_archivomd/DP2.png)
<br>

![3.-](https://github.com/DiegoIgnacioCorreaCervantes/Grafic/blob/main/Imagenes_archivomd/DP3.png)
<br>

![4.-](https://github.com/DiegoIgnacioCorreaCervantes/Grafic/blob/main/Imagenes_archivomd/DP4.png)
<br>

![5.-](https://github.com/DiegoIgnacioCorreaCervantes/Grafic/blob/main/Imagenes_archivomd/DP5.png)
<br>

![6.-](https://github.com/DiegoIgnacioCorreaCervantes/Grafic/blob/main/Imagenes_archivomd/DP6.png)
<br>

![7.-](https://github.com/DiegoIgnacioCorreaCervantes/Grafic/blob/main/Imagenes_archivomd/DP7.png)
<br>

![8.-](https://github.com/DiegoIgnacioCorreaCervantes/Grafic/blob/main/Imagenes_archivomd/DP8.png)
<br>

![9.-](https://github.com/DiegoIgnacioCorreaCervantes/Grafic/blob/main/Imagenes_archivomd/DP9.png)
<br>

![10.-](https://github.com/DiegoIgnacioCorreaCervantes/Grafic/blob/main/Imagenes_archivomd/DP10.png)
<br>

Cambiando la formula r obtenemos graficas distintas:

![](https://github.com/DiegoIgnacioCorreaCervantes/Grafic/blob/main/Imagenes_archivomd/DP11.png)
<br>

![Resultado](https://github.com/DiegoIgnacioCorreaCervantes/Grafic/blob/main/Imagenes_archivomd/DP12.png)
<br>

---
