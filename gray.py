import cv2

#input image
image = cv2.imread('new img.jpg')
cv2.imshow('Original', image)
cv2.waitKey(0)

#color img
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

cv2.imshow('Grayscale', gray_image)
cv2.waitKey(0)
