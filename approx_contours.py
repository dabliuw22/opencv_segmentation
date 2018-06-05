# -*- coding: utf-8 -*-
# Aproximar contornos
import cv2
import numpy as np

image = cv2.imread('/home/will/Imágenes/house.jpg')
original_image = image.copy()
cv2.imshow('Original', original_image)
cv2.waitKey(0)

# Obtenemos la imagen en escala de grises
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Obtenemos una representación binaria
ret, threshold = cv2.threshold(gray_image, 127, 255, cv2.THRESH_BINARY_INV)

# Obtenemos el array contornos
# Que obtenga todos los puntos (CHAIN_APPROX_NONE)
img, contornos, jerarquia = cv2.findContours(threshold, cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)

for c in contornos:
	x, y, w, h = cv2.boundingRect(c)
	cv2.rectangle(original_image, (x, y), (x + w, y + h), (0, 0, 255), 2)
	cv2.imshow('bounding rectangle', original_image)

cv2.waitKey(0)

for c in contornos:
	# Calculamos epsilon que es la distancia máxima entre el contorno 
	# y el contorno aproximado, se recomienda que sea menos de 5%. 
	epsilon = 0.01*cv2.arcLength(c,True)
	# figura aproximado para el contorno c
	approx = cv2.approxPolyDP(c, epsilon, True)
	cv2.drawContours(original_image, [approx], 0, (255, 255, 0), 2)
	cv2.imshow('Approx', original_image)

cv2.waitKey(0)
cv2.destroyAllWindows()