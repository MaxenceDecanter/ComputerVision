import cv2
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import gridspec

img = cv2.imread('bgr.png')

cv2.imshow('RGB Image', img)
key = cv2.waitKey(0)
if key == 27:
    cv2.destroyAllWindows()

blues = img[:, :, 0]
greens = img[:, :, 1]
reds = img[:, :, 2]

cv2.imshow('RGB Blues', blues)
cv2.imshow('RGB Greens', greens)
cv2.imshow('RGB Reds', reds)

key = cv2.waitKey(0)

shape = img.shape[0]
new_filter = np.zeros(shape=[shape, shape])

blue_filter = np.dstack((img[:, :, 0], new_filter, new_filter))
green_filter = np.dstack((new_filter, img[:, :, 1], new_filter))
red_filter = np.dstack((new_filter, new_filter, img[:, :, 2]))

cv2.imshow("Only blue", blue_filter)
cv2.imshow("Only green", green_filter)
cv2.imshow("Only red", red_filter)

key = cv2.waitKey(0)

added_image_rg = cv2.add(red_filter, green_filter)

cv2.imshow("added red green", added_image_rg)

added_image_final = cv2.add(added_image_rg, blue_filter)

cv2.imshow("added final", added_image_final)





key = cv2.waitKey(0)

if key == 27:
    cv2.destroyAllWindows()
cv2.destroyAllWindows()