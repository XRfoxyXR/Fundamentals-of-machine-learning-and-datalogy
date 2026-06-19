import numpy as np
import os

from skimage.io import imread
from skimage import img_as_float
from sklearn.cluster import KMeans

os.makedirs("Otvet", exist_ok=True)

image = imread("parrots.jpg")
image = img_as_float(image)

height, width, channels = image.shape
pixels = image.reshape(height * width, channels)


def psnr(original, compressed):
    mse = np.mean((original - compressed) ** 2)

    if mse == 0:
        return 100

    return 10 * np.log10(1.0 / mse)


answer = None

for n_clusters in range(1, 21):
    print("Кластеров:", n_clusters)

    kmeans = KMeans(
        n_clusters=n_clusters,
        init="k-means++",
        random_state=241,
        n_init=10
    )

    labels = kmeans.fit_predict(pixels)

    compressed_mean = np.zeros_like(pixels)
    compressed_median = np.zeros_like(pixels)

    for cluster in range(n_clusters):
        cluster_pixels = pixels[labels == cluster]

        mean_color = np.mean(cluster_pixels, axis=0)
        median_color = np.median(cluster_pixels, axis=0)

        compressed_mean[labels == cluster] = mean_color
        compressed_median[labels == cluster] = median_color

    compressed_mean_image = compressed_mean.reshape(height, width, channels)
    compressed_median_image = compressed_median.reshape(height, width, channels)

    psnr_mean = psnr(image, compressed_mean_image)
    psnr_median = psnr(image, compressed_median_image)

    print("PSNR mean:", psnr_mean)
    print("PSNR median:", psnr_median)
    print()

    if psnr_mean > 20 or psnr_median > 20:
        answer = n_clusters
        break

with open("Otvet/answer.txt", "w", encoding="utf-8") as file:
    file.write(str(answer))

print("Ответ:", answer)