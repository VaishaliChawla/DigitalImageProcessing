from PIL import Image
import numpy as np 
import cv2
import matplotlib.pyplot as plt
import math

class Morph:
	def __init__(self, imarr,k):
		self.img = imarr
		r,c = imarr.shape
		self.r = r
		self.c = c
		self.k = k
		self.k_cen = math.floor(k/2)

	def erosion(self):
		r_new = self.r-self.k+1
		c_new = self.c-self.k+1
		eroded = [[0 for i in range(c_new)]for j in range(r_new)]

		for a in range(0, self.r):
			for b in range(0,self.c):
				if a-self.k_cen>=0 and b-self.k_cen>=0:
					if a+self.k_cen<=(self.r-1) and b+self.k_cen<=(self.c-1):
						v = self.check(a,b,'e')
						eroded[a-self.k_cen][b-self.k_cen] = v
		return eroded
	
	def check(self,a,b,flag):
		for x in range(a-self.k_cen, a+self.k_cen+1):
			for y in range(b-self.k_cen, b+self.k_cen+1):
				if flag=='e' and self.img[x][y]==0:
					return 0
				if flag=='d' and self.img[x][y]==255:
					return 255
	
		if flag=='e':
			return 255
		elif flag=='d':
			return 0


	def dilation(self):
		r_new = self.r-self.k+1
		c_new = self.c-self.k+1
		dilated = [[0 for i in range(c_new)]for j in range(r_new)]

		for a in range(0, self.r):
			for b in range(0,self.c):
				if a-self.k_cen>=0 and b-self.k_cen>=0:
					if a+self.k_cen<=(self.r-1) and b+self.k_cen<=(self.c-1):
						v = self.check(a,b,'d')
						dilated[a-self.k_cen][b-self.k_cen] = v
		return dilated



im = cv2.imread("image_morph.jpg",0)
im = np.array(im, dtype=np.uint8)
m1 = Morph(im,3)
er = np.array(m1.erosion(), dtype=np.uint8)
di = np.array(m1.dilation(), dtype=np.uint8)

fig, ax = plt.subplots(4,2, figsize = (100,60))
ax[0][0].imshow(im)
ax[0][0].set_title("Image")
ax[0][0].axis("off")

ax[1][0].imshow(im)
ax[1][0].set_title("Image")
ax[1][0].axis("off")

ax[0][1].imshow(er)
ax[0][1].set_title("Eroded")
ax[0][1].axis("off")

ax[1][1].imshow(di)
ax[1][1].set_title("Dilated")
ax[1][1].axis("off")

im2 = cv2.imread("m_img.jpg",0)
im2 = np.array(im2, dtype=np.uint8)
m2 = Morph(im2,9)

ax[2][0].imshow(im2)
ax[2][0].set_title("Image")
ax[2][0].axis("off")

ax[3][0].imshow(im2)
ax[3][0].set_title("Image")
ax[3][0].axis("off")

ero = np.array(m2.erosion(), dtype = np.uint8)
m2_1 = Morph(ero,9)
opened = np.array(m2_1.dilation(), dtype = np.uint8)
ax[2][1].imshow(opened)
ax[2][1].set_title("Opened")
ax[2][1].axis("off")


dil = np.array(m2.dilation(), dtype = np.uint8)
m2_2 = Morph(dil,9)
closed = np.array(m2_2.erosion(), dtype = np.uint8)
ax[3][1].imshow(closed)
ax[3][1].set_title("Closed")
ax[3][1].axis("off")

plt.show()