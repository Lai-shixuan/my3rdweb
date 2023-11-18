from PIL import Image
import numpy as np
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

def remove_black_pixels(img, center, radius):
    width, height = img.size
    pixels = img.load()

    for i in range(width):
        for j in range(height):
            if (i-center[0])**2 + (j-center[1])**2 > radius**2:  # 如果像素位于圆形区域以外
                if pixels[i, j] == (0, 0, 0):  # 如果像素为黑色
                    pixels[i, j] = (255, 255, 255)  # 将黑色像素替换为白色
    return img

path = 'd:\GoogleDrive\\04 microCT土壤\\20231026 2次组会\\30μm-ROI36mm\q1.1 (315).bmp'

# 加载图像并转换为灰度
image = Image.open(path)

# 移除中心圆形区域以外的黑色像素，圆心为(width/2, height/2)，半径为min(width, height)/2
image = remove_black_pixels(image, (image.size[0]//2, image.size[1]//2), min(image.size)//2)

# image.show()

# 转换图像数据为numpy数组
image_np = np.array(image)

# 调整数组形状以适应KMeans函数，并归一化值
pixels = image_np.reshape(-1, 1) / 255.0

# 使用KMeans进行图像分割
kmeans = KMeans(n_clusters=2, random_state=0).fit(pixels)

# 使用KMeans模型的预测结果替换原来的像素值
segmented_img = kmeans.labels_.reshape(image_np.shape)

segmented_img = 1 - segmented_img

# 将segmented_img 保存到本地：
# test = Image.fromarray(segmented_img)
# test = segmented_img.convert('L')
# test.save('segmented.jpg', 'JPEG')

# 显示分割后的图像
plt.imshow(segmented_img, cmap='gray')
plt.savefig('segmented.jpg')
plt.show()