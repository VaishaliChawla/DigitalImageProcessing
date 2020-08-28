from PIL import Image
import numpy as np 
import cv2
import matplotlib.pyplot as plt
import math

img = cv2.imread("image_morph.jpg",0)
img = np.array(img, dtype=np.uint8)
r,c = img.shape

fig, ax = plt.subplots(4,2)
ax[0][0].imshow(img)
ax[0][0].set_title("Image")
ax[0][0].axis("off")

ax[1][0].imshow(img)
ax[1][0].set_title("Image")
ax[1][0].axis("off")

k = 3
kernel = [[255]*k]*k
k_cen = math.floor(k/2)

def check(a,b,flag):
	for x in range(a-k_cen, a+k_cen+1):
		for y in range(b-k_cen, b+k_cen+1):
			if flag=='e' and img[x][y]==0:
				return 0
			if flag=='d' and img[x][y]==255:
				return 255
	
	if flag=='e':
		return 255
	elif flag=='d':
		return 0

def erosion():
	r_new = r-k+1
	c_new = c-k+1
	eroded = [[0 for i in range(c_new)]for j in range(r_new)]

	for a in range(0, r):
		for b in range(0,c):
			if a-k_cen>=0 and b-k_cen>=0:
				if a+k_cen<=(r-1) and b+k_cen<=(c-1):
					v = check(a,b,'e')
					eroded[a-k_cen][b-k_cen] = v

	return eroded

def dilation():
	r_new = r-k+1
	c_new = c-k+1
	dilated = [[0 for i in range(c_new)]for j in range(r_new)]

	for a in range(0, r):
		for b in range(0,c):
			if a-k_cen>=0 and b-k_cen>=0:
				if a+k_cen<=(r-1) and b+k_cen<=(c-1):
					v = check(a,b,'d')
					dilated[a-k_cen][b-k_cen] = v
	return dilated

er = np.array(erosion(), dtype=np.uint8)
ax[0][1].imshow(er)
ax[0][1].set_title("Eroded")
ax[0][1].axis("off")

di = np.array(dilation(), dtype=np.uint8)
ax[1][1].imshow(di)
ax[1][1].set_title("Dilated")
ax[1][1].axis("off")


plt.show()