import cv2

# Load the image
img_path = r'D:\PYTHON\open_CV\paper.png'
img = cv2.imread(img_path)

# Convert image to grayscale
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Simple Thresholding
ret, thresh_binary = cv2.threshold(img_gray, 60, 255, cv2.THRESH_BINARY)

# Adaptive Thresholding
adaptive_thresh = cv2.adaptiveThreshold(img_gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 21, 30)


# Display images
cv2.imshow('Original Image', img)
cv2.imshow('Binary Threshold', thresh_binary)
cv2.imshow('Adaptive Threshold', adaptive_thresh)

cv2.waitKey(0)
cv2.destroyAllWindows()
