import cv2
import numpy as np
from skimage.feature import peak_local_max
from skimage.segmentation import watershed
from scipy import ndimage
import matplotlib.pyplot as plt

path = 'd:\GoogleDrive\\04 microCT土壤\\20231026 2次组会\\30μm-ROI36mm\q1.1 (315).bmp'

# 读取图像并转化为灰度图像
image = cv2.imread(path)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# 创建掩码，只保留图像中心的圆形区域
height, width = gray.shape
center_x, center_y = width // 2, height // 2
mask = np.zeros_like(gray)
cv2.circle(mask, (center_x, center_y), min(center_x, center_y), color=255, thickness=-1)

# 应用掩码并进行阈值化
gray = cv2.bitwise_and(gray, mask)
ret, thresh = cv2.threshold(gray,0,255,cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)

# 计算距离变换
distance = ndimage.distance_transform_edt(thresh)

# 获取局部最大值
coordinates = peak_local_max(distance, labels=thresh, min_distance=20)

# 为每一个局部最大值创建标签
labels = np.zeros(distance.shape, dtype=bool)
labels[coordinates[:, 0], coordinates[:, 1]] = 1
labels = ndimage.label(labels)[0]

# 应用分水岭算法
ws = watershed(-distance, labels, mask=thresh)

ws = np.where(ws > 0, 255, 0).astype(np.uint8)

cv2.imwrite("d:\\9-mysitewin\\DL\\a.jpg", ws)

# 展示结果
fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(12, 6),
                         sharex=True, sharey=True)
ax = axes.ravel()

ax[0].imshow(image, cmap=plt.cm.gray)
ax[0].set_title('Original Image')

ax[1].imshow(ws, cmap=plt.cm.gray)
ax[1].set_title('Segmented Image')

for a in ax:
    a.set_axis_off()

fig.tight_layout()
plt.show()