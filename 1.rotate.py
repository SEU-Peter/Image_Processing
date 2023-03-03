import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread("./pic/1.jpg")
print(f'type: {type(img)}')
plt.axis('off')
plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
plt.show()

# 对图像进行旋转
height, width = img.shape[:2]
print(img.shape)
print(height, width)
rotationMatrix = cv2.getRotationMatrix2D((width / 2, height / 2), 45, .5)
rotationImage = cv2.warpAffine(img, rotationMatrix, (width, height))
print(f'rotation image shape:{rotationImage.shape}')
plt.imshow(cv2.cvtColor(rotationImage, cv2.COLOR_BGR2RGB))
plt.show()



