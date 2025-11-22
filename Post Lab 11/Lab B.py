import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

# Load image
img = Image.open(r"C:\Users\Vrushank\Desktop\Python\MU.jpg")
img_array = np.array(img)

# Define padding size (top, bottom, left, right)
pad_top, pad_bottom, pad_left, pad_right = 50, 50, 50, 50

# Pad image with zeros (black)
padded_img = np.pad(img_array, ((pad_top, pad_bottom), (pad_left, pad_right), (0,0)), mode='constant', constant_values=0)

# Display using matplotlib
plt.figure(figsize=(8,8))
plt.imshow(padded_img)
plt.title("Padded Image")
plt.axis("off")
plt.show()