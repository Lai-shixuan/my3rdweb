from PIL import Image
import numpy as np

def calculate_histogram(image):
    histogram = np.zeros(256)
    for pixel in image:
        histogram[pixel] += 1
    return histogram / histogram.sum()

def otsu_threshold(histogram):
    total = 1
    current_max, threshold = 0, 0
    sumT, sumF, sumB = 0, 0, 0
    for i in range(0, 256):
        sumT += i * histogram[i]
    weightB = 0
    for i in range(0, 256):
        weightB += histogram[i]
        weightF = total - weightB
        if weightB == 0 or weightF == 0:
            continue
        sumB += i * histogram[i]
        sumF = sumT - sumB
        mB = sumB / weightB
        mF = sumF / weightF
        varBetween = weightB * weightF * (mB - mF) ** 2
        if varBetween > current_max:
            current_max = varBetween
            threshold = i
    return threshold

def apply_threshold(image, threshold):
    return image.point(lambda p: p > threshold and 255)

def otsu_method(image_path):
    image = Image.open(image_path).convert('L')
    histogram = calculate_histogram(image.getdata())
    threshold = otsu_threshold(histogram)
    return apply_threshold(image, threshold)

# 使用这个函数
binary_image = otsu_method('d:\GoogleDrive\\04 microCT土壤\\20231026 2次组会\\30μm-ROI36mm\q1.1 (315).bmp')
binary_image.show()