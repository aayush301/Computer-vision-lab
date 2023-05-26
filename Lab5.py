# Top 3 majoritarian gradients

import numpy as np
import matplotlib.pyplot as plt
import cv2



img1 = cv2.imread('../images/young.png',0)
img2 = cv2.imread('../images/old.png',0)

plt.figure()
plt.subplot(1,2,1)
plt.imshow(img1, cmap='gray')
plt.subplot(1,2,2)
plt.imshow(img2, cmap='gray')


(h,w) = img1.shape
img2 = cv2.resize(img2, (w,h))

block_h = int(h/4)
block_w = int(w/4)

imgs = [img1,img2]


print("Top three majoritarian gradients:")

for i in range(2):
	plt.figure()
	print("Image ", i+1)
	
	img = imgs[i]
	gradx = cv2.Sobel(img,-1,1,0,ksize=5)
	grady = cv2.Sobel(img,-1,0,1,ksize=5)
	gradxy = cv2.addWeighted(gradx, 0.5, grady, 0.5, 0)
	
	
	dir = np.zeros((h,w), dtype=np.int16)

	for i in range(h):
		for j in range(w):
			dir[i][j] = np.round(np.arctan2(grady[i][j],gradx[i][j])*180/np.pi)
	
	for x in range(4):
		for y in range(4):
			dir1 = dir[x*block_h : (x+1)*block_h, y*block_w : (y+1)*block_w]
			im = gradxy[x*block_h : (x+1)*block_h, y*block_w : (y+1)*block_w]
			plt.subplot(4,4,x*4+y+1)
			plt.imshow(im, cmap="gray")
			plt.xticks([])
			plt.yticks([])

			map = dict()
			for i in range(block_h):
				for j in range(block_w):
					if dir1[i][j] in map:
						map[dir1[i][j]]+=1
					else:
						map[dir1[i][j]]=1

			arr = sorted(map.items(), key=lambda x: x[1], reverse=True)

			print("(",x,",",y,") block: ", arr[0][0], arr[1][0], arr[2][0])
			plt.xlabel(str([arr[0][0], arr[1][0], arr[2][0]]))
			
			
plt.show()