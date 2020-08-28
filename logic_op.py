import numpy as np
import cv2
from matplotlib import pyplot as plt
from PIL import Image


def logic_and(a1,a2):
	rows,cols = a1.shape
	res_img = [[0 for x in range(cols)] for y in range(rows)]

	for x in range(rows):
		for y in range(cols):
			res_img[x][y] = a1[x][y] & a2[x][y]

	fig, ax = plt.subplots(1,3)
	ax[0].imshow(a1)
	ax[0].axis("off")
	ax[0].set_title("Image")

	ax[1].imshow(a2)
	ax[1].axis("off")
	ax[1].set_title("Mask")

	ax[2].imshow(res_img)
	ax[2].axis("off")
	ax[2].set_title("AND Result")
	plt.show()


def logic_or(a1, a2):

	rows, cols = a1.shape
	#creating mask
	im3 = [[0 for x in range(cols)] for y in range(rows)]
	for i in range(rows):
		for j in range(cols):
			im3[i][j] = 255-a2[i][j]

	or_result = [[0 for x in range(cols)] for y in range(rows)]

	for x in range(rows):
		for y in range(cols):
			or_result[x][y] = a1[x][y] | im3[x][y]

	fig, ax = plt.subplots(1,3)
	ax[0].imshow(a1)
	ax[0].axis("off")
	ax[0].set_title("Image")

	ax[1].imshow(im3)
	ax[1].axis("off")
	ax[1].set_title("Mask")

	ax[2].imshow(or_result)
	ax[2].axis("off")
	ax[2].set_title("OR Result")
	plt.show()

image1 = cv2.imread("car1.jpg",0)
im1_arr = np.array(image1, dtype=np.uint8)

image2 = cv2.imread("carthr.jpg",0)
im2_arr = np.array(image2, dtype=np.uint8)

logic_and(im1_arr,im2_arr)
logic_or(im1_arr,im2_arr)

