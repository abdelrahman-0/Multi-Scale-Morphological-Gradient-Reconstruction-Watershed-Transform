import numpy as np
import imutils
import cv2
from skimage.color import rgb2lab
from math import sqrt
from random import random as r
import matplotlib.pyplot as plt
from skimage.morphology import erosion, dilation, opening, closing, disk, reconstruction
from skimage.segmentation import mark_boundaries

from scipy import ndimage as ndi
from skimage.segmentation import watershed
from skimage.feature import peak_local_max
from random import uniform

def show_inplace(image):
    plt.axis('off')
    plt.imshow(image, cmap='gray')
    plt.show()
    
# Scale matrix values in [0,1] range    
def normalize(matrix):
    minimum = min([min(row) for row in matrix])
    temp = matrix - minimum
    maximum = max([max(row) for row in temp])
    temp = temp / maximum
    return temp
    
def full_grad(sobelx, sobely):
    result = np.sqrt(sobelx*sobelx + sobely*sobely)
    return normalize(result)
    
# Morphological reconstruction by closing (defined as dilation reconstruction followed by erosion reconstruction)
def mgr(img, kernel):
    e = erosion(img, kernel)
    r1 = reconstruction(e, img, method='dilation')
    d = dilation(r1, kernel)
    r2 = reconstruction(d ,r1, method='erosion')
    return r2

# Apply reconstruction by closing using kernels of different sizes. The point-wise maxima of all the reconstructions is taken to be the final result.
def mmgr(img, min_radius=1, max_iterations=50):
    result = np.zeros((img.shape)).astype(img[0][0])
    prev = result.copy()
    iterations = 0
    for i in range(max_iterations):
        prev = result
        se = disk(min_radius+i)
        gr = mgr(img, se)
        result = np.maximum(result, gr)
        if (prev == result).all():
            break
        iterations += 1
    print('Number of iterations till convergence: ', iterations)
    return result

# Use mean color of pixels to colour the superpixel
def color_superpixels(superpixels, original):
    result = original.copy()
    rows, cols = superpixels.shape
    for val in np.unique(superpixels):
        result[superpixels == val] = np.mean(original[superpixels == val], axis=0)
    return result
