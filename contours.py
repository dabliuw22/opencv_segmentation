# -*- coding: utf-8 -*-
import cv2
import numpy as np

image = cv2.imread('/home/will/Imágenes/ubuntu.png')

# Obtenemos la imagen en escala de grises
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Obtenemos una representación binaria
ret, threshold = cv2.threshold(gray_image, 127, 255, cv2.THRESH_BINARY_INV)
cv2.imshow('Binaria', threshold)
cv2.waitKey(0)

# Obtenemos una imagen con bordes
edged = cv2.Canny(threshold, 30, 200)
cv2.imshow('Edged Image', edged)
cv2.waitKey(0)

# Obtenemos el array contornos
# Que obtenga todos los puntos (CHAIN_APPROX_NONE)
img, contornos, jerarquia = cv2.findContours(edged, cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
#img, contornos, jerarquia = cv2.findContours(edged, cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)
cv2.imshow('Contours', edged)
cv2.waitKey(0)

# Dibujamos todos los puntos de los contornos (-1)
# Con el color (0, 255, 0) y el grosor de 2px  
cv2.drawContours(image, contornos, -1, (0, 255, 0), 2)
cv2.imshow('Imagen', image)
cv2.waitKey(0)

cv2.destroyAllWindows()