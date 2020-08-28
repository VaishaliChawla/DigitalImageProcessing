import numpy as np 
import cv2 
import matplotlib.pyplot as plt 


image1 = cv2.imread("pic1.jpg")
im1_arr = np.array(image1, dtype = np.uint8)

image2 = cv2.imread("pic2.jpg")
im2_arr = np.array(image2, dtype = np.uint8)

difference = np.subtract(im1_arr,im2_arr)


fig,ax = plt.subplots(1,3)
ax[0].imshow(im1_arr)
ax[0].axis("off")
ax[0].set_title("Image 1")

ax[1].imshow(im2_arr)
ax[1].axis("off")
ax[1].set_title("Image 2")

ax[2].imshow(difference)
ax[2].axis("off")
ax[2].set_title("Image 1 - Image 2")

plt.show()