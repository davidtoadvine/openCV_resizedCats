


import cv2

ow_img = cv2.imread("cat.jpg")
rudy_img = cv2.imread("fat.jpg")

window1 = cv2.namedWindow("w1")

scale_percent = 25
width = int(ow_img.shape[1]*scale_percent /100)
height = int(ow_img.shape[0] * scale_percent/100)

ow_resized = cv2.resize(ow_img, (width, height), interpolation=cv2.INTER_AREA)
rudy_resized = cv2.resize(rudy_img, (width, height), interpolation=cv2.INTER_AREA)

cv2.imshow(window1, ow_resized)
cv2.waitKey(8000)

cv2.imshow(window1, rudy_resized)
cv2.waitKey(8000)



