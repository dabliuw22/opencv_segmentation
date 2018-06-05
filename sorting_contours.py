# -*- coding: utf-8 -*-
# Ordenanando Contornos
import cv2
import numpy as np

def get_contour_areas(contours):
	all_areas = []
	for c in contours:
		area = cv2.contourArea(c)
		all_areas.append(area)
	return all_areas

image = cv2.imread('/home/will/Imágenes/figuras.png')
original_image = image.copy()

# Obtenemos la imagen en escala de grises
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Obtenemos una representación binaria
ret, threshold = cv2.threshold(gray_image, 127, 255, cv2.THRESH_BINARY_INV)

# Obtenemos el array contornos
# Que obtenga todos los puntos (CHAIN_APPROX_NONE)
img, contornos, jerarquia = cv2.findContours(threshold, cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)

# Clasificar contornos de mayor a menor (reverse = True)
sorted_contours = sorted(contornos, key = cv2.contourArea, reverse = True)

for c in sorted_contours:
	# Dibujar todos los puntos del contorno [c] en la imagen original
	cv2.drawContours(original_image, [c], -1, (255, 255, 0), 2)
	cv2.waitKey(0)
	cv2.imshow('Contours by area', original_image)

cv2.waitKey(0)
cv2.destroyAllWindows()