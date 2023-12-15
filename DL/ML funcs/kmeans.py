from PIL import Image
import numpy as np
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import cv2


def remove_black_pixels(img, center, radius):
    width, height = img.size
    # img = img.convert('RGBA')
    # pixels = img.load()
    image_np = np.array(img)

    alpha_channel = np.full(image_np.shape, 255, dtype=np.uint8)
    np_img_with_alpha = np.stack((image_np, alpha_channel), axis=-1)

    for i in range(height):
        for j in range(width):
            if (i - center[0]) ** 2 + (j - center[1]) ** 2 > radius ** 2:  # 如果像素位于圆形区域以外
                # if pixels[i, j] == (0, 0, 0, 0):  # 如果像素为黑色
                np_img_with_alpha[i, j] = (0, 0)  # 将黑色像素替换为白色
    return np_img_with_alpha


for i in range(16):
    path = ('d:\\GoogleDrive\\04 microCT土壤\\20231026 2次组会\\'
            '30μm-ROI36mm\\q1.1 (' + str(i + 300) + ').bmp')

    # 加载图像并转换为灰度
    image = Image.open(path)

    # 移除中心圆形区域以外的黑色像素，圆心为(width/2, height/2)，半径为min(width, height)/2
    image = remove_black_pixels(image, (image.size[0] // 2, image.size[1] // 2), min(image.size) // 2)

    # 转换图像数据为numpy数组
    # image_np = np.array(image)

    # 调整数组形状以适应KMeans函数，并归一化值
    # new index to get the image
    image_reshaped = image.reshape(-1, 2)
    index = image_reshaped[:, 1] == 255
    image_shrink = image_reshaped[index] / 255.0

    pixels = image_shrink[:, 0].reshape(-1, 1)

    # 使用KMeans进行图像分割
    kmeans = KMeans(n_clusters=2, random_state=0).fit(pixels)

    # 使用KMeans模型的预测结果替换原来的像素值
    pixels_km = kmeans.labels_

    counter = 0
    for j, flag in enumerate(index):
        if flag:
            image_reshaped[j, 0] = pixels_km[counter]
            counter = counter + 1
    segmented_img = image_reshaped.reshape(image.shape)

    # Separate the channels
    gray = segmented_img[:, :, 0] * 255
    alpha = segmented_img[:, :, 1]
    alpha = np.expand_dims(alpha, axis=-1)

    # Convert grayscale to a 3-channel BGR image
    bgr = cv2.cvtColor(gray, cv2.COLOR_GRAY2BGR)
    bgra = np.concatenate((bgr, alpha), axis=-1)
    # bgra = cv2.merge([bgr, alpha])

    # if sum(sum(segmented_img))/1204/1204 > 0.5:
    #     segmented_img = 1 - segmented_img

    cv2.imwrite("segmented" + str(i) + ".png", bgra)
