import cv2
#sumando
img1=cv2.imread('cadena.jpg',0)
img2=cv2.imread('sacapuntas.jpg',0)

resA = cv2.add(img1,img2)

#print(img1[0:3,0:3])
#print(img2[0:3,0:3])
#print(resA[0:3,0:3])

cv2.imshow('resA',resA)
cv2.imshow('img1',img1)
cv2.imshow('img2',img2)

cv2.waitKey(0)
cv2.destroyAllWindows()