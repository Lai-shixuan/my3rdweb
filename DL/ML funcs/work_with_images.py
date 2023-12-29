from PIL import Image
import numpy as np
import cv2
import os
from functions import method_PositionIndependent as mPI
from functions import method_PositionDepentent as mPD
import configparser
import math

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
    elif text == 'watershed':
        return mPD.watershed


# Read a grayscale img, give it a transparent layer. It doesn't cut the image.
def remove_black_pixels(img):
    alpha_channel = np.full(img.shape, 255, dtype=np.uint8)
    np_img_with_alpha = np.stack((img, alpha_channel), axis=-1)
    height, width = img.shape

    for i in range(height):
        for j in range(width):
            if (i - width // 2) ** 2 + (j - height // 2) ** 2 > (min(height, width)/2) ** 2:  # 如果像素位于圆形区域以外
                # if pixels[i, j] == (0, 0, 0, 0):  # 如果像素为黑色
                np_img_with_alpha[i, j] = (0, 0)  # 将黑色像素替换为白色
    return np_img_with_alpha


# The first thing is to read and merge all images.
def pi_integrate_images(input_folder, radius):
    img_files = sorted([os.path.join(input_folder, f) for f in os.listdir(input_folder)
                        if f.endswith('.bmp') or f.endswith('.png')])

    stacked = []

    for img_file in img_files:
        # 加载图像并转换为灰度
        image = Image.open(img_file)
        width, height = image.size
        image = image.crop((width // 2 - radius, height // 2 - radius, width // 2 + radius, height // 2 + radius))
        width, height = image.size
        image_np = np.array(image)

        # 移除中心圆形区域以外的黑色像素，圆心为(width/2, height/2)，半径为min(width, height)/2
        image = remove_black_pixels(image_np)

        stacked.append(image)

    stacked = np.array(stacked)
    return stacked


def pi_segment(images, name):
    # 调整数组形状以适应KMeans函数，并归一化值
    image_reshaped = images.reshape(-1, 2)
    index = image_reshaped[:, 1] == 255
    image_shrink = image_reshaped[index] / 255.0
    pixels = image_shrink[:, 0].reshape(-1, 1)

    # 调用函数进行图像分割，输入和输出的像素都是0-1之间
    segmentor = method_choose(name)
    segmented_number = segmentor(pixels)

    # df = pd.DataFrame({'Pixels': pixels.flatten(), 'Segmented number': segmented_number})
    # df.to_csv(output_folder + f'\\_{i}_{method_name}.csv', index=False)

    # 进行替换，将分类后的标签数据重新回填到原始图片中
    counter = 0
    for j, flag in enumerate(index):
        if flag:
            image_reshaped[j, 0] = segmented_number[counter] * 255
            counter = counter + 1
    result = image_reshaped.reshape(images.shape)
    return result


def pd_segment(path, radius):

    img_files = sorted([os.path.join(path, f) for f in os.listdir(path)
                        if f.endswith('.bmp') or f.endswith('.png')])
    stacked = []

    for img_file in img_files:
        img = cv2.imread(img_file, cv2.IMREAD_GRAYSCALE)
        height, width = img.shape
        img = img[(height // 2 - radius):(height // 2 + radius), (width // 2 - radius):(width // 2 + radius)]
        img = mPD.watershed(img)
        stacked.append(img)

    stacked = np.array(stacked)
    return stacked


def export_images(images, path, radius, method_genre):
    for i, image in enumerate(images):

        if method_genre == 'PD':
            image = remove_black_pixels(image)

        # Separate the channels
        gray = image[:, :, 0]
        alpha = image[:, :, 1]
        alpha = np.expand_dims(alpha, axis=-1)

        # 控制孔隙用哪一个标签表示
        if np.sum(gray) / 255 / (radius ** 2 * math.pi) > 0.5:
            gray = 255 - gray

        # Convert grayscale to a 3-channel BGR image
        bgr = cv2.cvtColor(gray, cv2.COLOR_GRAY2BGR)
        bgra = np.concatenate((bgr, alpha), axis=-1)

        cv2.imwrite(path + '\\' + str(radius) + '_' + method_name
                    + '_segmented' + f"{i:04d}" + '.png', bgra)


config = configparser.ConfigParser()
config.read('config.ini')
input_path = config['DEFAULT']['input_path']
ROI = int(config['DEFAULT']['ROI'])
method_name = config['DEFAULT']['method_name']
output_path = config['DEFAULT']['output_path']
if method_name != 'watershed':
    method_genre = 'PI'
else:
    method_genre = 'PD'

if method_genre == 'PI':
    stacked_images = pi_integrate_images(input_path, ROI)
    segmented_images = pi_segment(stacked_images, method_name)
elif method_genre == 'PD':
    segmented_images = pd_segment(input_path, ROI)
export_images(segmented_images, output_path, ROI, method_genre)
