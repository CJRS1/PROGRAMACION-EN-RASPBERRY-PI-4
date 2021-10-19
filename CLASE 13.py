import cv2
import numpy as np

imagen = 255*np.ones((400,600,3),dtype=np.uint8)


#dibujandio linea
cv2.line(imagen,(0,0),(600,400),(255,0,0),4)
#dibujando rectangulo
cv2.rectangle(imagen,(50,80),(200,200),(0,255,0),4)
#dibujando circulo
cv2.circle(imagen,(300,200),100,(0,0,255),-1)

font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(imagen,'Practicando con OpenCV',(10,30),font,1,(0,255,255),2,cv2.LINE_AA)
cv2.putText(imagen,'Practicando con OpenCV',(10,60),0,1,(0,255,255),2,cv2.LINE_AA)
cv2.putText(imagen,'Practicando con OpenCV',(10,90),1,1,(0,255,255),2,cv2.LINE_AA)
cv2.putText(imagen,'Practicando con OpenCV',(10,120),2,1,(0,255,255),2,cv2.LINE_AA)
cv2.putText(imagen,'Practicando con OpenCV',(10,150),3,1,(0,255,255),2,cv2.LINE_AA)
cv2.putText(imagen,'Practicando con OpenCV',(10,180),4,1,(0,255,255),2,cv2.LINE_AA)
cv2.putText(imagen,'Practicando con OpenCV',(10,210),5,1,(0,255,255),2,cv2.LINE_AA)
cv2.putText(imagen,'Practicando con OpenCV',(10,240),6,1,(0,255,255),2,cv2.LINE_AA)
cv2.putText(imagen,'Practicando con OpenCV',(10,30),7,1,(0,255,255),2,cv2.LINE_AA)


cv2.imshow('imagen',imagen)
cv2.waitKey(0)
cv2.destroyAllWindows()