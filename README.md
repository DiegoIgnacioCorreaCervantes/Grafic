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

![Ejecución](https://github.com/DiegoIgnacioCorreaCervantes/Grafic/blob/main/Imagenes_archivomd/pixelart_ejecucion.png)

---
