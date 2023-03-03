import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread("./pic/guitar.png")
height, width = img.shape[:2]
print(f'origin image shape:{img.shape}')

# 中值滤波主要消除椒盐噪声和斑点噪声
blur_img = cv2.medianBlur(img, 5)
plt.figure(figsize=(32, 32))
plt.subplot(1, 2, 1)
plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
plt.subplot(1, 2, 2)
plt.imshow(cv2.cvtColor(blur_img, cv2.COLOR_BGR2RGB))
plt.show()
