import cv2
import numpy as np 
import imutils

# imutils redimensiona imagen
image = cv2.imread('imagen.jpg',0)
image=imutils.resize(image,width=400)

#_,binarizada = cv2.threshold(image,210,255,cv2.THRESH_BINARY)
#_,binarizadaInv = cv2.threshold(image,210,255,cv2.THRESH_BINARY_INV)
#_,Trunc=cv2.threshold(image,210,255,cv2.THRESH_TRUNC)
_,Toz=cv2.threshold(image,210,255,cv2.THRESH_TOZERO)
_,TozInv=cv2.threshold(image,210,255,cv2.THRESH_TOZERO_INV)


cv2.imshow('Imagen',image)
#cv2.imshow('Tipos: Binary - Binary Inv',np.hstack([binarizada,binarizadaInv]))
#cv2.imshow('Tipos:Trunc',Trunc)
cv2.imshow('Tipos:Tozero - Tozero Inv',np.hstack([Toz,TozInv]))

cv2.waitKey(0)
cv2.destroyAllWindows()