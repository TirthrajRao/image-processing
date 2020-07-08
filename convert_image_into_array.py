# source : https://www.pluralsight.com/guides/importing-image-data-into-numpy-arrays


from PIL import Image
from numpy import asarray
# load the image
image = Image.open('pr_train_1.jpg')
# convert image to numpy array
img1 = image.copy()
# print(image.)
data = asarray(img1)
print(len(data[0]))
for pixel in data[0]:
	print(pixel[0])
	pixel[0] = 0	

for pixel in data[0]:
	print(pixel[0])
# summarize shape
print(data.shape)

# create Pillow image
image2 = Image.fromarray(data)
print(type(image2))

# summarize image details
print(image2.mode)
print(image2.size)