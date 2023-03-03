import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread("./pic/guitar.png")
height, width = img.shape[:2]
print(f'origin image shape:{img.shape}')

edge_img = cv2.Canny(img, 100, 200) # minVal 和 maxVal 分别表示梯度强度值的最小值和最大值
plt.figure(figsize=(32, 32))
plt.subplot(1, 2, 1)
plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
plt.subplot(1, 2, 2)
plt.imshow(cv2.cvtColor(edge_img, cv2.COLOR_BGR2RGB))
plt.show()