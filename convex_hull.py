# -*- coding: utf-8 -*-
# Cascara convexa
import cv2
import numpy as np

image = cv2.imread('/home/will/Imágenes/mano.png')
original_image = image.copy()
cv2.imshow('Original', original_image)
cv2.waitKey(0)

# Obtenemos la imagen en escala de grises
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Obtenemos una representación binaria
ret, threshold = cv2.threshold(gray_image, 127, 255, cv2.THRESH_BINARY_INV)

# Obtenemos el array contornos
# Que obtenga todos los puntos (CHAIN_APPROX_NONE)
img, contornos, jerarquia = cv2.findContours(threshold.copy(), cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)

# Obtenemos el número de contornos, ordenamos
# de menor a mayor
n = len(contornos)
print(n)
# Si tenemos un contorno grande (marco), 
# podemos eliminarlo n = len(contornos) -1
contornos = sorted(contornos, key = cv2.contourArea, reverse = False)[:n]

for c in contornos:
	hull = cv2.convexHull(c)
	cv2.drawContours(original_image, [hull], 0, (0, 255, 0), 2)
	cv2.imshow('Convex Hull', original_image)

cv2.waitKey(0)
cv2.destroyAllWindows()