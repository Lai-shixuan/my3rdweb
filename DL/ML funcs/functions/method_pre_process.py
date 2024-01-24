import cv2
import numpy as np


def origin(img):
    return img


def adjust_gamma(img, gamma=1):
    inv_gamma = 1.0 / gamma
    table = np.array([((i / 255.0) ** inv_gamma) * 255
                      for i in np.arange(0, 256)]).astype("uint8")
    # 应用伽马校正
    return cv2.LUT(img, table)


def equalized_hist(img):
    return cv2.equalizeHist(img)


def median(img, kernel_size=3):
    return cv2.medianBlur(img, kernel_size)
