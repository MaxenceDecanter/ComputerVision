
from opencv import cv2
import numpy as np


reference = ['comparaison.jpg', 'comparaison2.jpg', 'comparaison3.jpg', 'comparaison4.jpg']



for ref in reference:

    img_rgb = cv2.imread('dog.jpg')
    img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)

    template = cv2.imread(ref, 0)
    w, h = template.shape[::-1]

    res = cv2.matchTemplate(img_gray, template, cv2.TM_CCOEFF_NORMED)
    threshold = 0.96
    loc = np.where(res >= threshold)

    for pt in zip(*loc[::-1]):
        cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0, 255, 255), 2)
        cv2.imshow("Detected in "+ref, img_rgb)



"""cv2.imshow('Detected', img_rgb)"""
cv2.waitKey(0)
cv2.destroyAllWindows()


