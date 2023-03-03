import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread("./pic/1.jpg")
height, width = img.shape[:2]
print(f'origin image shape:{img.shape}')

# 调整图像的对比度
# 高对比度
high_contrast_img = cv2.addWeighted(img, 2.5, np.zeros(img.shape, img.dtype), 0, 0)
# 低对比度
low_contrast_img = cv2.addWeighted(img, 0.5, np.zeros(img.shape, img.dtype), 0, 0)
plt.figure(figsize=(32, 16))
plt.subplot(3, 1, 1)
plt.title('origin image')
plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
plt.subplot(3, 1, 2)
plt.title('hight contrast image')
plt.imshow(cv2.cvtColor(high_contrast_img, cv2.COLOR_BGR2RGB))
plt.subplot(3, 1, 3)
plt.title('low contrast image')
plt.imshow(cv2.cvtColor(low_contrast_img, cv2.COLOR_BGR2RGB))
plt.show()