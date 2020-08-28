from PIL import Image
import numpy as np 
import cv2
import matplotlib.pyplot as plt
import math

o = cv2.imread("parrot.jpg",0)
orgimg = np.array(o, dtype=np.uint8)
ht, wd = orgimg.shape
#print("ORG",ht,",",wd)

fig,ax = plt.subplots(1,2)
ax[0].imshow(orgimg)
ax[0].axis("off")
ax[0].set_title("Original Image")

f = 7
f_cent = math.floor(f/2)
avgfil = [[1]*f]*f
ht_new = ht-f+1
wd_new = wd-f+1
new_img = [[0 for x in range(wd_new)] for y in range(ht_new)]
#print(np.array(new_img).shape)

def compute_mask(i,j):
	value = 0
	for a in range(i-f_cent, i+f_cent+1):
		for b in range(j-f_cent, j+f_cent+1):
			value += orgimg[a][b]
	return value


for i in range(ht):
	for j in range(wd):
		if i-f_cent>=0 and j-f_cent>=0:
			if i+f_cent<=(ht-1) and j+f_cent<=(wd-1):
				value = compute_mask(i,j)
				new_img[i-f_cent][j-f_cent] = round(value/(f*f))


bp = Image.fromarray(np.array(new_img, dtype = np.uint8))
bp.save("blurparrot.jpg")

ax[1].imshow(np.array(new_img))
ax[1].axis("off")
ax[1].set_title("After avaeraging")
plt.show()