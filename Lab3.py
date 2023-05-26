# Implement the Image transforms and apply on the 2-D image

import numpy as np
import matplotlib.pyplot as plt
import cv2


# Walsh-Hadamard Transform
U = cv2.imread('./images/landscape-scenery.jpg',0)
N = U.shape[0]
N = 2**int(np.log2(N))
U = cv2.resize(U,(N,N))
print(U.shape)


n = int(np.log2(N))
H1 =np.array([[1,1],[1,-1]])
H = np.array([[1,1],[1,-1]])

for i in range(n-1):
    H = np.kron(H,H1)
    
H = H/(2**(n/2))
print(H)

V = np.matmul(np.matmul(H,U),H)
plt.imshow(V, cmap='gray')