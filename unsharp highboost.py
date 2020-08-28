from PIL import Image
import numpy as np 
import cv2
import matplotlib.pyplot as plt

p = cv2.imread("parrot.jpg",0)
p_arr = np.array(p, dtype = np.uint8)
ht, wd = p_arr.shape
print("ORG ", ht,",",wd)

fig,ax = plt.subplots(1,4)
ax[0].imshow(np.array(p_arr, dtype = np.uint8))
ax[0].axis("off")
ax[0].set_title("Original Image")


o = cv2.imread("blurparrot.jpg",0)
#org = cv2.copyMakeBorder(o, top=1, bottom=1, left=1, right=1, borderType=cv2.BORDER_DEFAULT)
orgimg = np.array(o, dtype=np.uint8)
ht2, wd2 = orgimg.shape
print("BLUR",ht2,",",wd2)

t = int((ht-ht2)/2)
b = t
l = int((wd-wd2)/2)
r = l

org = cv2.copyMakeBorder(o, top = t, bottom = b, left = l, right = r, borderType=cv2.BORDER_DEFAULT)
orgimg = np.array(org, dtype=np.uint8)

ax[1].imshow(orgimg)
ax[1].axis("off")
ax[1].set_title("Blur Image")

mask = np.subtract(p_arr, orgimg)

#unsharp masking
final_img = np.add(p_arr, mask)
unsharp_img = Image.fromarray(final_img)
unsharp_img.save("UnsharpImg.jpg")

ax[2].imshow(np.array(final_img, dtype = np.uint8))
ax[2].axis("off")
ax[2].set_title("Resultant Image")


#highboost filtering
k = 4
mask2 = mask*k
final_img2 = np.add(p_arr, mask2)
high = Image.fromarray(final_img2)
high.save("HighboostImg.jpg")

ax[3].imshow(np.array(final_img2, dtype=np.uint8))
ax[3].axis("off")
ax[3].set_title("High Boost Image")
plt.show()