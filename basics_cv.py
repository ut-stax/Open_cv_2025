import cv2

# Define the image path
img_path = r"D:\PYTHON\open_CV\buttt.jpg"

# Read the image
img = cv2.imread(img_path)

# write the image
# cv2.imwrite((r"D:\PYTHON\open_CV\butt.jpg"),img)

# visualize the image
# cv2.imshow('frame', img)
# cv2.waitKey(0)

# Learn how to work videos 

# How to work with WebCam
# webcam = cv2.VideoCapture(0)
# while True:
#     ret, frame = webcam.read()

#     cv2.imshow('frame',frame)
#     if cv2.waitKey(40) & 0xFF == ord('q'):
#         break

# webcam.release()
# cv2.destroyAllWindows()

# How to Rezise Image
# resized_img= cv2.resize(img,(420,240))
# cv2.imshow('Original Image', img)
# cv2.imshow('Resized Image', resized_img)
# cv2.waitKey(0)

height, width, channels = img.shape

# Print the image size
print(f"Image Dimensions: {width}x{height}")
print(f"Number of Channels: {channels}")

# How to Crop Image
print(img.shape)
cropped_img = img[0:400, 0:800]
cv2.imshow('corpped',cropped_img)
cv2.waitKey(0)
