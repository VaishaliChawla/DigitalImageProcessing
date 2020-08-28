from PIL import Image
import numpy as np 
import cv2
import matplotlib.pyplot as plt

o = cv2.imread("blurparrot.jpg",0)
#org = cv2.copyMakeBorder(o, top=1, bottom=1, left=1, right=1, borderType=cv2.BORDER_DEFAULT)
orgimg = np.array(o, dtype=np.uint8)
ht, wd = orgimg.shape
print("ORG",ht,",",wd)

fig,ax = plt.subplots(1,2)
ax[0].imshow(orgimg)
ax[0].axis("off")
ax[0].set_title("Original Image")

lap = np.array([[0,1,0],[1,-4,1],[0,1,0]])
ht_new = ht-3+1
wd_new = wd-3+1
new_img = [[0 for x in range(wd_new)] for y in range(ht_new)]

def laplacian_fil(i,j):
	value = int(orgimg[i][j-1]) + int(orgimg[i][j+1]) + int(orgimg[i+1][j]) + int(orgimg[i-1][j]) - 4*int(orgimg[i][j])
	return value

for i in range(ht):
	for j in range(wd):
		if i-1>=0 and j-1>=0:
			if i+1<=(ht-1) and j+1<=(wd-1):
				value = laplacian_fil(i,j)
				new_img[i-1][j-1] = value

#final_img = np.subtract(orgimg,new_img)

lap_img = Image.fromarray(np.array(new_img, dtype = np.uint8))
lap_img.save("Laplacedimg.jpg")
ax[1].imshow(np.array(new_img, dtype = np.uint8))
ax[1].axis("off")
ax[1].set_title("Sharpened Image")
plt.show()