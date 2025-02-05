import os
import cv2

img_path = r'D:\PYTHON\open_CV\butt.jpg'
img = cv2.imread(img_path)
cv2.imshow('original',img)
# Cartitian Blur 
k_size = 71
img_blur = cv2.blur(img,(k_size,k_size))
cv2.imshow('blur',img_blur)
# Gaussian Blur (Must be an odd number and not too large)
img_gaussian_blur = cv2.GaussianBlur(img,(k_size,k_size),5)
cv2.imshow('blur2',img_gaussian_blur)
# Medina Blur 
img_median_blur = cv2.medianBlur(img,k_size)
cv2.imshow('median_blur',img)

cv2.waitKey(0)
