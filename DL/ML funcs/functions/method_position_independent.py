import cv2
import numpy as np
from sklearn.cluster import KMeans
from sklearn.mixture import GaussianMixture


# non-parameter methods
def otsu(numbers):
    numbers = numbers.reshape(-1, 1)
    numbers_8u = np.uint8(numbers)
    _, dst = cv2.threshold(numbers_8u, 0, 255, cv2.THRESH_OTSU)
    return dst


def kapur_entropy(image):
    # Calculate histogram of the image
    image = image.reshape(-1, 1)
    image = np.uint8(image)
    hist = cv2.calcHist([image], [0], None, [256], [0, 256]).ravel()
    hist = hist / hist.sum()

    # Compute cumulative sum and cumulative mean
    cum_sum = hist.cumsum()

    # Initialize variables
    max_ent = 0.0
    optimal_threshold = 0.0

    t_list = []

    entropy_list = []

    # kapur's entropy method
    for t in range(256):
        omega_a = cum_sum[t]
        if omega_a > 0.01 and 1 - omega_a > 0.01:
            t_list.append(t)

    for t in t_list:
        omega_a = cum_sum[t]
        omega_b = cum_sum[-1] - omega_a
        # Calculate entropy
        entropy_a = -np.sum(hist[t_list[0]:t+1] / omega_a * np.log(hist[t_list[0]:t+1] / omega_a))
        entropy_b = -np.sum(hist[t+1:t_list[-1]] / omega_b * np.log(hist[t+1:t_list[-1]] / omega_b))
        total_entropy = entropy_a + entropy_b
        entropy_list.append([t, total_entropy])

        # Check if new maximum entropy is found
        if total_entropy > max_ent:
            max_ent = total_entropy
            optimal_threshold = t

    # Apply threshold to the image
    _, threshold_image = cv2.threshold(image, optimal_threshold, 255, cv2.THRESH_BINARY)

    return threshold_image.flatten()


def kmeans(numbers):
    numbers = numbers.reshape(-1, 1)
    numbers = numbers / 255
    kmeans_filter = KMeans(n_clusters=2, random_state=0).fit(numbers)
    classes = kmeans_filter.labels_
    return classes * 255


def gmm(numbers):
    numbers = numbers.reshape(-1, 1)
    numbers = numbers / 255
    gmm_filter = GaussianMixture(n_components=2, random_state=0).fit(numbers)
    pixels_gmm = gmm_filter.predict(numbers)
    return pixels_gmm * 255
