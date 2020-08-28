import numpy as np
import cv2
import math
from PIL import Image
from scipy import ndimage
from matplotlib import pyplot as plt

def robert_edge_det(image):
	robert_h = np.array([[0,0,0], [0,0,1], [0,-1,0]])
	robert_v = np.array([[0,0,0], [0,1,0],[0,0,-1]])

	v_edge = ndimage.convolve(image, robert_v)
	h_edge = ndimage.convolve(image, robert_h)

	res = np.round(np.sqrt( np.square(v_edge) + np.square(h_edge)))
	return res


def sobel_edge_det(image):
	sobel_h = np.array([[-1,-2,-1],[0,0,0],[1,2,1]])
	sobel_v = np.array([[-1,0,1],[-2,0,2],[-1,0,1]])

	v_edge = ndimage.convolve(image, sobel_v)
	h_edge = ndimage.convolve(image, sobel_h)

	#res2 = np.round(np.sqrt( np.square(v_edge) + np.square(h_edge)))
	return v_edge, h_edge

 
input_image = cv2.imread("Bikesgray.jpg",0)
inp_arr = np.array(input_image)

fig, ax = plt.subplots(1,4)
ax[0].imshow(inp_arr)
ax[0].axis("off")
ax[0].set_title("Image")

result = robert_edge_det(inp_arr)
r = Image.fromarray(np.array(result, dtype = np.uint8))
r.save("Roberts.jpg")

ax[1].imshow(np.array(result, dtype = np.uint8))
ax[1].axis("off")
ax[1].set_title("Roberts")


v,h = sobel_edge_det(inp_arr)
v2 = Image.fromarray(v)
v2.save("Sobel_v.jpg")

h2 = Image.fromarray(h)
h2.save("Sobel_h.jpg")

ax[2].imshow(np.array(v, dtype = np.uint8))
ax[2].axis("off")
ax[2].set_title("Sobel_v")

ax[3].imshow(np.array(h, dtype = np.uint8))
ax[3].axis("off")
ax[3].set_title("Sobel_h")

plt.show()