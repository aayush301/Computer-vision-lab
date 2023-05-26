# Optical Flow

import cv2
import numpy as np
import matplotlib.pyplot as plt

cap = cv2.VideoCapture("../videos/car1.mp4")
feature_params = dict(maxCorners = 100, qualityLevel = 0.3, minDistance = 7, blockSize = 7)

of_params = dict(winSize = (15,15), maxLevel = 2, criteria = (cv2.TermCriteria_EPS | cv2.TermCriteria_COUNT, 10, 0.03))


# Create some random colors
color = np.random.randint(0,255,(100,3))

ret, old_frame = cap.read()
old_gray = cv2.cvtColor(old_frame, cv2.COLOR_BGR2GRAY)

p0 = cv2.goodFeaturesToTrack(old_gray, mask=None, **feature_params)

mask = np.zeros_like(old_frame)

while(1):
	ret,frame = cap.read()
	new_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	
	p1, st, err = cv2.calcOpticalFlowPyrLK(old_gray, new_gray, p0, None, **of_params)
	good_new = p1[st==1]
	good_old = p0[st==1]
	
	for i, (new,old) in enumerate(zip(good_new, good_old)):
		a,b = new.ravel()
		c,d = old.ravel()
		a = int(a)
		b = int(b)
		c = int(c)
		d = int(d)
		mask = cv2.line(mask, (a,b), (c,d), color[i].tolist(), 5)
		frame = cv2.circle(frame, (a,b), 5, color[i].tolist(), -1)
	
	img = cv2.add(frame, mask)
	cv2.imshow("frame", img)
	k = cv2.waitKey(30) & 0xff
	if k==27:
		break
	
	old_gray = new_gray.copy()
	
	p0 = good_new.reshape(-1,1,2)

cv2.destroyAllWindows()
