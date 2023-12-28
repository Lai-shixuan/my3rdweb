from PIL import Image
import numpy as np
import cv2
import os
from functions import method_PositionIndependent as mPI
import pandas as pd


def method_choose(text):
    if text == 'kmeans':
        return mPI.kmeans
    elif text == 'gmm':
        return mPI.gmm
    elif text == 'otsu':
        return mPI.otsu
    elif text == 'kapur_entropy':
        return mPI.kapur_entropy


# other functions
def remove_black_pixels(img, radius):
    width, height = img.size
    img = img.crop((width // 2 - radius, height // 2 - radius, width // 2 + radius, height // 2 + radius))
    width, height = img.size
    image_np = np.array(img)

    alpha_channel = np.full(image_np.shape, 255, dtype=np.uint8)
    np_img_with_alpha = np.stack((image_np, alpha_channel), axis=-1)

    for i in range(height):
        for j in range(width):
            if (i - width // 2) ** 2 + (j - height // 2) ** 2 > radius ** 2:  # 如果像素位于圆形区域以外
                # if pixels[i, j] == (0, 0, 0, 0):  # 如果像素为黑色
                np_img_with_alpha[i, j] = (0, 0)  # 将黑色像素替换为白色
    return np_img_with_alpha


def work_with_images(input_folder, output_folder, radius, method_name):
    img_files = sorted([os.path.join(input_folder, f) for f in os.listdir(input_folder)
                        if f.endswith('.bmp') or f.endswith('.png')])

    for i, img_file in enumerate(img_files):
        # 加载图像并转换为灰度
        image = Image.open(img_file)

        # 移除中心圆形区域以外的黑色像素，圆心为(width/2, height/2)，半径为min(width, height)/2
        image = remove_black_pixels(image, radius)

        # 调整数组形状以适应KMeans函数，并归一化值
        image_reshaped = image.reshape(-1, 2)
        index = image_reshaped[:, 1] == 255
        image_shrink = image_reshaped[index] / 255.0
        pixels = image_shrink[:, 0].reshape(-1, 1)

        # 调用函数进行图像分割，输入和输出的像素都是0-1之间
        segmentor = method_choose(method_name)
        segmented_number = segmentor(pixels)

        df = pd.DataFrame({'Pixels': pixels.flatten(), 'Segmented number': segmented_number})
        df.to_csv(output_folder + f'\\_{i}_{method_name}.csv', index=False)

        # 进行替换，将分类后的标签数据重新回填到原始图片中
        counter = 0
        for j, flag in enumerate(index):
            if flag:
                image_reshaped[j, 0] = segmented_number[counter]
                counter = counter + 1
        segmented_img = image_reshaped.reshape(image.shape)

        # Separate the channels
        gray = segmented_img[:, :, 0]
        alpha = segmented_img[:, :, 1]
        alpha = np.expand_dims(alpha, axis=-1)

        # 控制孔隙用哪一个标签表示
        if np.sum(gray) / (radius ** 2) > 0.5:
            gray = 1 - gray

        # Convert grayscale to a 3-channel BGR image
        bgr = cv2.cvtColor(gray * 255, cv2.COLOR_GRAY2BGR)
        bgra = np.concatenate((bgr, alpha), axis=-1)

        cv2.imwrite(output_folder + '\\' + str(radius) + '_' + method_name
                    + '_segmented' + f"{i:04d}" + '.png', bgra)


input_path = 'D:\\9-mysitewin\\DL\\ML funcs\\data\\origin'
output_path = 'D:\\9-mysitewin\\DL\\ML funcs\\data\\result'
ROI = 150
method_name = 'kapur_entropy'

work_with_images(input_path, output_path, ROI, method_name)
