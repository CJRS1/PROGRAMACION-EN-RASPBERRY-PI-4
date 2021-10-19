import cv2
#sumando
img1=cv2.imread('cadena.jpg',0)
img2=cv2.imread('sacapuntas.jpg',0)

res1 = cv2.subtract(img1,img2)
res2 = cv2.absdiff(img1,img2)

cv2.imshow('res1',res1)
cv2.imshow('res2',res2)
#cv2.imshow('img1',img1)
#cv2.imshow('img2',img2)

cv2.waitKey(0)
cv2.destroyAllWindows()
#https://docs.opencv.org/master/d2/de8/group__core__array.html#gafafb2513349db3bcff51f54ee5592a19