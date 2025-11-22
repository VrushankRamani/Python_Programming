import numpy as np
from PIL import Image

# Load the image
img = Image.open(r"C:\Users\Vrushank\Desktop\Python\MU.jpg")
img_array = np.array(img)

print("Image dimensions (height x width):", img_array.shape[0], "x", img_array.shape[1])
print("Image shape (H x W x Channels):", img_array.shape)
print("Minimum pixel value per channel:", img_array.min(axis=(0,1)))
print("Maximum pixel value per channel:", img_array.max(axis=(0,1)))