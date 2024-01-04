import numpy as np
import cv2
import os
from functions import method_position_independent as mpi
from functions import method_position_dependent as mpd
import configparser
from tqdm import tqdm

import pandas as pd


def method_choose(text):
    if text == 'kmeans':
        return mpi.kmeans
    elif text == 'gmm':
        return mpi.gmm
    elif text == 'otsu':
        return mpi.otsu
    elif text == 'kapur_entropy':
        return mpi.kapur_entropy
    elif text == 'watershed':
        return mpd.watershed


# The first thing is to read and merge all images.
def integrate_images(input_folder, radius):
    img_files = sorted([os.path.join(input_folder, f) for f in os.listdir(input_folder)
                        if f.endswith('.bmp') or f.endswith('.png')])

    stacked = []

    for img_file in img_files:
        # 加载图像并转换为灰度
        image = cv2.imread(img_file, cv2.IMREAD_GRAYSCALE)
        width, height = image.shape
        img = image[(height // 2 - radius):(height // 2 + radius), (width // 2 - radius):(width // 2 + radius)]

        # image = remove_black_pixels(img)
        stacked.append(img)

    stacked = np.array(stacked)
    return stacked


def segment(images, name, dependent):
    segmentor = method_choose(name)

    if dependent:
        for i in tqdm(range(images.shape[0])):
            images[i] = segmentor(images[i])
    else:
        # 调整数组形状以适应KMeans函数，并归一化值
        image_reshaped = images.reshape(-1, 1)
        segmented_number = segmentor(image_reshaped)
        images = segmented_number.reshape(images.shape)

    # df = pd.DataFrame({'Pixels': pixels.flatten(), 'Segmented number': segmented_number})
    # df.to_csv(output_folder + f'\\_{i}_{method_name}.csv', index=False)
    return images


def export_images(images, path, radius):
    for i, image in enumerate(images):

        # # 控制孔隙用哪一个标签表示
        # if np.sum(image) / 255 / (radius ** 2 * 4) > 0.5:
        #     image = 255 - image

        cv2.imwrite(path + '\\' + str(radius) + '_' + method_name
                    + '_segmented' + f"{i:04d}" + '.png', image)


config = configparser.ConfigParser()
config.read('config.ini')
input_path = config['DEFAULT']['input_path']
ROI = int(config['DEFAULT']['ROI'])
method_name = config['DEFAULT']['method_name']
output_path = config['DEFAULT']['output_path']
if method_name == 'watershed':
    method_dependent = True
else:
    method_dependent = False

stacked_images = integrate_images(input_path, ROI)
segmented_images = segment(stacked_images, method_name, method_dependent)
export_images(segmented_images, output_path, ROI)

# Below is something not going to use it.

# Read a grayscale img, give it a transparent layer. It doesn't cut the image.
# def remove_black_pixels(img):
#     alpha_channel = np.full(img.shape, 255, dtype=np.uint8)
#     np_img_with_alpha = np.stack((img, alpha_channel), axis=-1)
#     height, width = img.shape
#
#     for i in range(height):
#         for j in range(width):
#             if (i - width // 2) ** 2 + (j - height // 2) ** 2 > (min(height, width)/2) ** 2:
#             # 如果像素位于圆形区域以外
#                 # if pixels[i, j] == (0, 0, 0, 0):  # 如果像素为黑色
#                 np_img_with_alpha[i, j] = (0, 0)  # 将黑色像素替换为白色
#     return np_img_with_alpha

# 这是一个函数的一部分，为了进行替换，将分类后的标签数据重新回填到原始图片中。但是当时是因为圆形图片相当于有空白像素，
# 因此只能建立索引，然后一个一个按照顺序回填
# counter = 0
# for j, flag in enumerate(index):
#     if flag:
#         image_reshaped[j, 0] = segmented_number[counter] * 255
#         counter = counter + 1
