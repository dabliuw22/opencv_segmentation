# -*- coding: utf-8 -*-
# Detección de círculos con la transformada de círculo de Hough
import cv2
import numpy as np

image = cv2.imread('/home/will/Imágenes/tapitas.jpg')
cv2.imshow('Circulos detectados',image)
cv2.waitKey(0)

# Obtenemos la imagen en escala de grises
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Aplicamos filtrado
blur = cv2.medianBlur(gray_image, 5)

# Obtenemos los circulos
circulos = cv2.HoughCircles(image = blur, method = cv2.HOUGH_GRADIENT,
	dp = 1.5, minDist = 10)

#circulos = np.uint16(np.around(circulos))
for c in circulos[0, :]:
	# Dibujar los circulos
	cv2.circle(image,(c[0], c[1]), c[2], (255, 0, 0), 2)
	# Dibujar el centro de los circulos
	cv2.circle(image, (c[0], c[1]), 2, (0, 255, 0), 5)

cv2.imshow('Circulos detectados',image)
cv2.waitKey(0)
cv2.destroyAllWindows()
