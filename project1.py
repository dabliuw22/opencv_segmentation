# -*- coding: utf-8 -*-
# Identificando formas
import cv2
import numpy as np

# Función que devuelve el centroide de un contorno
def centroide(contorno):
	M = cv2.moments(contorno)
	cx = int(M['m10']/M['m00'])
	cy = int(M['m01']/M['m00'])
	centroide = (cx, cy)
	return centroide

def figura(contorno):
	# Calculamos epsilon que es la distancia máxima entre el contorno 
	# y el contorno aproximado, se recomienda que sea menos de 5%. 
	epsilon = 0.01*cv2.arcLength(contorno, True)
	# figura aproximado para el contorno c
	approx = cv2.approxPolyDP(contorno, epsilon, True)
	num_lados = len(approx)
	if num_lados == 3:
		nombre_figura = 'Triangulo'
		color = (0, 255, 0)
	elif num_lados == 4:
		x, y, w, h = cv2.boundingRect(contorno)
		print(x, y, w, h, abs(w-x), abs(h-y))
		if w == h:
			nombre_figura = 'Cuadrado'
			color = (0, 125, 255)
		else:
			nombre_figura = 'Rectangulo'
			color = (0, 0, 255)
	elif num_lados == 10:
		nombre_figura = 'Estrella'
		color = (255, 255, 0)
	elif num_lados >= 15:
		nombre_figura = 'Circulo'
		color = (0, 255, 255)
	return [nombre_figura, color, approx]

def operation():
	image = cv2.imread('/home/will/Imágenes/figuras.png')
	cv2.imshow('Identificando formas', image)
	cv2.waitKey(0)

	# Obtenemos la imagen en escala de grises
	gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

	# Obtenemos una representación binaria
	ret, threshold = cv2.threshold(gray_image, 127, 255, cv2.THRESH_BINARY_INV)

	# Obtenemos el array contornos
	img, contornos, jerarquia = cv2.findContours(threshold, cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)

	for c in contornos:
		nombre_figura, color, approx = figura(c)
		# Buscamos el centroide del contorno para colocar el texto
		cx, cy = centroide(c)
		cv2.drawContours(image, [approx], 0, color, -1)
		cv2.putText(image, nombre_figura, (cx - 50, cy), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 1)

		cv2.imshow('Identificando formas', image)
		cv2.waitKey(0)
	cv2.destroyAllWindows()

operation()