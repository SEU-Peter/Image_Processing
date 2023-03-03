import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread("./pic/1.jpg")
height, width = img.shape[:2]
print(f'origin image shape:{img.shape}')

# 对图像进行切分
start_row = int(height * 0.15)
start_col = int(width * 0.15)
end_row = int(height * 0.85)
end_col = int(width * 0.85)

cropped_image = img[start_row:end_row, start_col:end_col]
print(f'crop image shape:{cropped_image.shape}')

plt.axis('off')
plt.imshow(cv2.cvtColor(cropped_image, cv2.COLOR_BGR2RGB))
plt.show()
