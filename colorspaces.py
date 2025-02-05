import os
import cv2
img_path = r"D:\PYTHON\open_CV\butt.jpg"
img = cv2.imread(img_path)




# cv2.cvtColor() this function is used to deal with the colours spaces in openvc
img_rgb = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
img_gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
img_hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
cv2.imshow('original',img)
cv2.imshow('rgb',img_rgb)
cv2.imshow('gray',img_gray)
cv2.imshow('hsv',img_hsv)
cv2.waitKey(0)
cv2.destroyAllWindows()
