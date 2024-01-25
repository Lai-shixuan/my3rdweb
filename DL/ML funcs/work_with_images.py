import numpy as np
import cv2
import os
import configparser
from tqdm import tqdm
import threading
import time
from functions.method_choose import seg_method_choose

import pandas as pd
from datetime import datetime


# The first thing is to read and merge all images.
def integrate_images(input_folder, radius):
    img_files = sorted([os.path.join(input_folder, f) for f in os.listdir(input_folder)
                        if f.endswith('.bmp') or f.endswith('.png')])

    stacked = []

    for i, img_file in enumerate(img_files):
        # 加载图像并转换为灰度

        image = cv2.imread(img_file, cv2.IMREAD_GRAYSCALE)
        # width, height = image.shape
        # img = image[(height // 2 - radius):(height // 2 + radius), (width // 2 - radius):(width // 2 + radius)]
        img = image[(430 - radius):(430 + radius), (450 - radius):(450 + radius)]

        # image = remove_black_pixels(img)
        stacked.append(img)

    stacked = np.array(stacked)
    print('The images are integrated.')
    return stacked


def segment(images, name):
    global stop_thread
    segmentor, independent = seg_method_choose(name)

    print('Ready to segment the images.')

    result_images = np.zeros_like(images)

    if not independent:
        for i in tqdm(range(images.shape[0])):
            result_images[i] = segmentor(images[i])
    else:
        indicator_thread = threading.Thread(target=show_running_time)
        indicator_thread.daemon = True
        indicator_thread.start()

        # 3D images is the input, and [-1, ] array are output
        segmented_number = segmentor(images)
        result_images = segmented_number.reshape(images.shape)

    # Only for pandas export to examine whether the independent method
    # is single threshold or not
    pixels = images.reshape([-1, ])
    # global output_path
    # now = datetime.now()
    # dt_string = now.strftime("%d%m%Y_%H%M%S")
    # df = pd.DataFrame({'Pixels': pixels, 'Segmented number': result_images.reshape([-1, ])})
    # df.to_csv(f'{output_path}\\{method_name}_{dt_string}.csv', index=False)

    print('Segmentation is finished.')
    stop_thread = True

    return result_images


def export_images(images, path, radius):
    for i, image in enumerate(images):

        # # 控制孔隙用哪一个标签表示
        # if np.sum(image) / 255 / (radius ** 2 * 4) > 0.5:
        #     image = 255 - image

        cv2.imwrite(path + '\\' + str(radius) + '_' + method_name
                    + '_segmented' + f"{i:04d}" + '.png', image)


def show_running_time():
    global stop_thread
    start_time = time.time()
    while not stop_thread:
        duration = time.time() - start_time
        print(f'The segmentation has spent {duration:.0f}s of time', end='\r', flush=True)
        time.sleep(5)


stop_thread = False
config = configparser.ConfigParser()
config.read('config.ini')
input_path = config['DEFAULT']['input_path']
ROI = int(config['DEFAULT']['ROI'])
method_name = config['DEFAULT']['method_name']
output_path = config['DEFAULT']['output_path']

print(f'The input path is {input_path}')
print(f'The output path is {output_path}')
print(f'The method name is {method_name}')
print(f'The radius is {ROI}')
stacked_images = integrate_images(input_path, ROI)
segmented_images = segment(stacked_images, method_name)
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
