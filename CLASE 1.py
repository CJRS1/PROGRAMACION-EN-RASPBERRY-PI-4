import cv2

imagen = cv2.imread("imagen.jpg",0)
cv2.imshow("imagen",imagen)
cv2.imwrite("grises.jpg",imagen)
cv2.waitKey(0)
cv2.destroyAllWindows()
