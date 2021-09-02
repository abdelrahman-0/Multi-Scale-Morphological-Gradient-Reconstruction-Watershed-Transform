# Multi-Scale Morphological Gradient Reconstruction Watershed-Transform (MMGR-WT)
A color-based superpixel algorithm. MMGR uses a composition of morphological operators to remove small local minima in the gradient image before applying the watershed transform (WT).

Histsorically, the WT algorithm was known for its sever over-segmentation (as shown in the first row of the image). In order to address this problem, MMGR attempts to preprocess the gradient image before applying WT. This reduces the over-segementation (as shown in the second row of the image).

<p float="left">
  <img src="/comparison.png" width="600" />
</p>

References:

Lei, Tao, et al. "Superpixel-based fast fuzzy C-means clustering for color image segmentation." IEEE Transactions on Fuzzy Systems 27.9 (2018): 1753-1766.
