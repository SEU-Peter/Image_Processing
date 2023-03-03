import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread("./pic/1.jpg")
height, width = img.shape[:2]
print(f'origin image shape:{img.shape}')

# 按照一定的比例进行缩放，图像不会产生形变
new_img = cv2.resize(img, (0, 0), fx=0.75, fy=0.75)
print(f'new img shape:{new_img.shape}')
plt.axis('off')
plt.imshow(cv2.cvtColor(new_img, cv2.COLOR_BGR2RGB))
plt.show()

# 缩放到指定的大小，会产生一些形变
new_img = cv2.resize(img, (800, 800))
print(f'new img shape:{new_img.shape}')
plt.axis('off')
plt.imshow(cv2.cvtColor(new_img, cv2.COLOR_BGR2RGB))
plt.show()