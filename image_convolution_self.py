import numpy as np
import cv2 
from matplotlib import pyplot as plt
from PIL import Image, ImageFilter
# %matplotlib inline
image = cv2.imread('pr_train_1.jpg') # reads the image
print(len(image))

image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)



def convolutionImage(topLeft, topMiddle, topRight, middleLeft, middle, middleRight, bottomLeft, bottomMiddle, bottomRight):
	arr = []
	
	first = (int(topLeft[0])) + (int(topMiddle[0])) + (int(topRight[0])) + (int(middleLeft[0])) + (int(middle[0])) + (int(middleRight[0])) + (int(bottomLeft[0])) + (int(bottomMiddle[0])) + (int(bottomRight[0]))
	first = first / 5
	arr.append(first)
	# arr.append((topLeft[0] + topMiddle[0] + topRight[0] + middleLeft[0] + middle[0] + middleRight[0] + bottomLeft[0] + bottomMiddle[0] + bottomRight[0])/ 9)
	arr.append(((int(topLeft[1])) + (int(topMiddle[1])) + (int(topRight[1])) + (int(middleLeft[1])) + (int(middle[1])) + (int(middleRight[1])) + (int(bottomLeft[1])) + (int(bottomMiddle[1])) + (int(bottomRight[1])))/ 5)
	arr.append(((int(topLeft[2])) + (int(topMiddle[2])) + (int(topRight[2])) + (int(middleLeft[2])) + (int(middle[2])) + (int(middleRight[2])) + (int(bottomLeft[2])) + (int(bottomMiddle[2])) + (int(bottomRight[2])))/ 5)
	return arr


image1 = image.copy();
i = 0
for pixel in range(len(image1)):
	j = 0
	for pix in range(len(image1[i])):
		arr = []
		arr.append(int(image1[i][j][0]) + int(image1[i][j][1]) + int(image1[i][j][2]))
		print(arr)
		image1[i][j] = arr
		j = j + 1
	i = i + 1

print(image1[0][699], len(image1[0]), len(image1))

# i = 0
# # image1[0][0] = [0, 0, 0]
# # i ==> row
# # j ==> coloumn
# i = 0
# for i in range(len(image1)):
# 	# print("row ===> ", i)	
# 	j = 0
# 	finalSt = ''
# 	for j in range(len(image1[i])): 
# 		if(i != 0) and (i != len(image1) - 1) and (j != 0) and (j != len(image1[i]) - 1):
# 			image1[i][j] = convolutionImage(image1[i-1][j-1], image1[i-1][j], image1[i-1][j+1], 
# 				image1[i][j-1], image1[i][j], image1[i][j+1],
# 				image1[i+1][j-1], image1[i+1][j], image1[i+1][j+1])			
# 			
# 		j = j + 1
# 	# print("\n")



# print("i ==> ", i, " j ===> ", j)


# half = cv2.resize(image, (0, 0), fx = 0.5, fy = 0.5) 
half = cv2.resize(image1, (0, 0), fx = 0.5, fy = 0.5) 

cv2.imshow('hello', half)
cv2.waitKey(0)  



# plt.figure(figsize=(12,6))
# plt.subplot(121), plt.imshow(cv2.cvtColor(image, cv2.COLOR_HSV2RGB)),plt.title('Original')
# plt.xticks([]), plt.yticks([])
# plt.subplot(122), plt.imshow(cv2.cvtColor(image1, cv2.COLOR_HSV2RGB)),plt.title('Mean filter')
# plt.xticks([]), plt.yticks([])
# plt.show()








# image = cv2.imread('./pr_train_1.jpg') # reads the image
# image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV) # convert to HSV
# figure_size = 9 # the dimension of the x and y axis of the kernal.
# new_image = cv2.blur(image,(figure_size, figure_size))
# plt.figure(figsize=(11,6))
# plt.subplot(121), plt.imshow(cv2.cvtColor(image, cv2.COLOR_HSV2RGB)),plt.title('Original')
# plt.xticks([]), plt.yticks([])
# plt.subplot(122), plt.imshow(cv2.cvtColor(new_image, cv2.COLOR_HSV2RGB)),plt.title('Mean filter')
# plt.xticks([]), plt.yticks([])
# plt.show()