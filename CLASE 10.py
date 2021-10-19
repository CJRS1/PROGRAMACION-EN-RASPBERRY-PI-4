import cv2
import numpy as np 

cap = cv2.VideoCapture(0)

#azulBajo=np.array([100,100,20],np.uint8)
#azulAlto=np.array([125,255,255],np.uint8)

#azulBajo=np.array([0,100,20],np.uint8)
#azulAlto=np.array([8,255,255],np.uint8)

azulBajo=np.array([175,100,20],np.uint8)
azulAlto=np.array([179,255,255],np.uint8)

while True: 
	ret,frame = cap.read()
	if ret == True:
		#transforma imagen a HSV
		frameHSV = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
		#se genera mascara
		mask = cv2.inRange(frameHSV,azulBajo,azulAlto)
		#genera un contorno
		contornos,_ =cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
		
		for c in contornos:
			area = cv2.contourArea(c)
			#si area es grande sí dibuja, sino no
			if area>3000:
				cv2.drawContours(frame,[c],0,(0,0,255),3)
		#cv2.drawContours(frame,contornos,-1,(255,0,0),3)
		#-1 dibuja todos los contornos
		#cv2.imshow('mask',mask)
		cv2.imshow('frame',frame)
		if cv2.waitKey(1)&0xFF == ord('s'):
			break

cap.release()
cv2.destroyAllWindows()