import cv2
import numpy as np

class RegionGrowing:
    def __init__(self, img):
        self.image = img
        self.height, self.width = img.shape
        self.seeds = [(self.width//2, self.height//2)]  # 设定种子点为图像中心
        self.visited = np.zeros_like(self.image, dtype=np.bool_)

    def grow(self, threshold=30):
        image_mean = np.mean(self.image)
        # 将图像分为亮部分和暗部分
        self.image = np.where(self.image < image_mean, 0, 255)

        # 创建一个与原始图像同样大小的图像
        segmented = np.zeros_like(self.image, dtype=np.uint8)

        while len(self.seeds) > 0:
            s = self.seeds.pop(0)

            x, y = s[0], s[1]

            if not (0 <= x < self.width and 0 <= y < self.height):
                continue

            if self.visited[x, y]:
                continue

            self.visited[x, y] = True

            if abs(int(self.image[x, y]) - int(self.image[self.width//2, self.height//2])) > threshold:
                continue

            segmented[x, y] = 255

            # 将邻居点添加到种子列表中
            self.seeds.append((x+1, y))
            self.seeds.append((x-1, y))
            self.seeds.append((x, y+1))
            self.seeds.append((x, y-1))

        return segmented

# 读取图像
path = 'd:\GoogleDrive\\04 microCT土壤\\20231026 2次组会\\30μm-ROI36mm\q1.1 (315).bmp'

img = cv2.imread(path, cv2.IMREAD_GRAYSCALE)

# 初始化区域生长算法
rg = RegionGrowing(img)

# 运行区域生长算法
result = rg.grow()

# 显示结果
# cv2.imshow('Segmented Image', result)
cv2.imwrite('segmented-regionGrowing.jpg', result)
# cv2.waitKey(0)
# cv2.destroyAllWindows()