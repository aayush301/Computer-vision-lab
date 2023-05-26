# Plot histograms for parts of two images- unnoisy and noisy

import matplotlib.pyplot as plt
import cv2


ny=4
nx=4


img = cv2.imread('./images/unnoisy-image.jpg',0)
h = int(img.shape[0]/ny)
w = int(img.shape[1]/nx)

plot_no=1
for i in range(ny):
    for j in range(nx):
        part = img[i*h:(i+1)*h,j*w:(j+1)*w]
        plt.subplot(ny,nx,plot_no)
        plt.imshow(part, cmap='gray')
        plot_no+=1

plt.suptitle('Unnoisy image')
plt.show()

plot_no=1
for i in range(ny):
    for j in range(nx):
        part = img[i*h:(i+1)*h,j*w:(j+1)*w]
        part = part.flatten()
        plt.subplot(ny,nx,plot_no)
        hist = cv2.calcHist([part],[0], None, [256], [0,256])
        plt.plot(hist)
        plot_no+=1

plt.suptitle('Histograms for Unnoisy image')
plt.show()




img = cv2.imread('./images/noisy-image.png',0)
h = int(img.shape[0]/ny)
w = int(img.shape[1]/nx)

plot_no=1
for i in range(ny):
    for j in range(nx):
        part = img[i*h:(i+1)*h,j*w:(j+1)*w]
        plt.subplot(ny,nx,plot_no)
        plt.imshow(part, cmap='gray')
        plot_no+=1

plt.suptitle('Noisy image')
plt.show()

plot_no=1
for i in range(ny):
    for j in range(nx):
        part = img[i*h:(i+1)*h,j*w:(j+1)*w]
        part = part.flatten()
        plt.subplot(ny,nx,plot_no)
        hist = cv2.calcHist([part],[0], None, [256], [0,256])
        plt.plot(hist)
        plot_no+=1

plt.suptitle('Histograms for noisy image')
plt.show()