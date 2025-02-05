import os
import cv2

img_path = r'D:\PYTHON\open_CV\apple.jpg'

img = cv2.imread(img_path)
cv2.imshow('frame',img)

#Thresholding 
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(img_gray, 80,255,cv2.THRESH_BINARY)
thresh = cv2.blur(thresh,(10,10))
ret, thresh = cv2.threshold(thresh, 80,255,cv2.THRESH_BINARY)


cv2.imshow('thresh', thresh)

cv2.waitKey(0)