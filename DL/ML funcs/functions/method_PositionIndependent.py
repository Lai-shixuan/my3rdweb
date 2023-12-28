import cv2
import numpy as np
from sklearn.cluster import KMeans
from sklearn.mixture import GaussianMixture


# non-parameter methods
def otsu(numbers):
    numbers_8u = np.uint8(numbers * 255)
    _, dst = cv2.threshold(numbers_8u, 0, 255, cv2.THRESH_OTSU)
    return dst / 255


def kapur_entropy(image):
    # Calculate histogram of the image
    image = np.uint8(image * 255)
    hist = cv2.calcHist([image], [0], None, [256], [0, 256]).ravel()
    hist = hist / hist.sum()

    # Compute cumulative sum and cumulative mean
    cumsum = hist.cumsum()
    cummean = np.cumsum(hist * np.arange(256))

    # Initialize variables
    alpha = 0.0
    beta = 0.0
    max_ent = 0.0

    # Kapur's entropy method
    for t in range(256):
        alpha += hist[t]
        if alpha == 0 or alpha == 1:
            continue

        beta = 1.0 - alpha
        omegaA = cumsum[t]
        omegaB = cumsum[-1] - omegaA
        muA = cummean[t] / omegaA
        muB = (cummean[-1] - cummean[t]) / omegaB

        # Calculate entropy
        entropyA = -np.sum(hist[:t+1] / alpha * np.log(hist[:t+1] / alpha + np.finfo(float).eps))
        entropyB = -np.sum(hist[t+1:] / beta * np.log(hist[t+1:] / beta + np.finfo(float).eps))
        total_entropy = entropyA + entropyB

        # Check if new maximum entropy is found
        if total_entropy > max_ent:
            max_ent = total_entropy
            optimal_threshold = t

    # Apply threshold to the image
    _, thresholded_image = cv2.threshold(image, optimal_threshold, 255, cv2.THRESH_BINARY)

    return thresholded_image.flatten()/255


def kmeans(numbers):
    kmeans_filter = KMeans(n_clusters=2, random_state=0).fit(numbers)
    classes = kmeans_filter.labels_
    return classes


def gmm(numbers):
    gmm_filter = GaussianMixture(n_components=2, random_state=0).fit(numbers)
    pixels_gmm = gmm_filter.predict(numbers)
    return pixels_gmm
