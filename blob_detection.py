# -*- coding: utf-8 -*-
# Detección de blob (manchas) comunes
import cv2
import numpy as np

image = cv2.imread('/home/will/Imágenes/girasoles.jpg', cv2.IMREAD_GRAYSCALE)
cv2.imshow('Girasoles',image)
cv2.waitKey(0)

# Creamos un detector con parametros por deault.
detector = cv2.SimpleBlobDetector_create()

# Detectar blobs.
blobs_points = detector.detect(image)

zeros = np.zeros((1, 1))

blobs = cv2.drawKeypoints(image, blobs_points, zeros,
	(0, 255, 255), cv2.DRAW_MATCHES_FLAGS_DEFAULT)

cv2.imshow('Girasoles', blobs)
cv2.waitKey(0)
cv2.destroyAllWindows()