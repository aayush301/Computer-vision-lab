# SIFT

import numpy as np
import matplotlib.pyplot as plt
import cv2

img = cv2.imread('../images/landscape-scenery.jpg',0)

h = img.shape[0]
w = img.shape[1]

def gaussianBlur(i,j,sigma):
    return (1/(2*np.pi*sigma*sigma))*np.exp(-(i*i+j*j)/(2*sigma*sigma))
    
sigma = 1
bimg= [[0 for j in range(w)] for i in range(h)]
for i in range(h):
    for j in range(w):
        bimg[i][j] = gaussianBlur(i,j,sigma)*img[i][j]

print(bimg)
plt.imshow(img, cmap='gray')
plt.show()
plt.imshow(bimg, cmap='gray')
plt.show()