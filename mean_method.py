import numpy as np
import cv2 
from matplotlib import pyplot as plt
from PIL import Image, ImageFilter
# %matplotlib inline
image = cv2.imread('pr_train_1.jpg') # reads the image
print(len(image))


image1 = image.copy();
i = 0
# image1[0][0] = [0, 0, 0]
# i ==> coloumn
# j ==> Row
i = 0
for i in range(len(image1)):
	# print("row ===> ", i)	
	j = 0
	for j in range(len(image1[i])): 
		if(i < len(image1)):
			if(j < len(image1[i]) -1 ):
				image1[i][j] = image1[i][j - 1] 
		j = j + 1
	i = i + 1	


print(image1[0][699], len(image1[0]), len(image1))


half = cv2.resize(image1, (0, 0), fx = 0.5, fy = 0.5) 

cv2.imshow('hello', half)
cv2.waitKey(0)  


# image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV) # convert to HSV
figure_size = 9 # the dimension of the x and y axis of the kernal.
# new_image = cv2.blur(image,(figure_size, figure_size))
# plt.figure(figsize=(11,6))
# plt.xticks([]), plt.yticks([])
# plt.subplot(122), plt.imshow(cv2.cvtColor(new_image, cv2.COLOR_HSV2RGB)),plt.title('Mean filter')
# plt.xticks([]), plt.yticks([])
plt.show()