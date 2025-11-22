import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

# Load image
img = Image.open(r"C:\Users\Vrushank\Desktop\Python\MU.jpg")
img_array = np.array(img)

# Function to show one channel
def show_channel(channel_name):
    channel = img_array.copy()
    if channel_name == 'R':
        channel[:,:,1] = 0  # Zero Green
        channel[:,:,2] = 0  # Zero Blue
    elif channel_name == 'G':
        channel[:,:,0] = 0  # Zero Red
        channel[:,:,2] = 0  # Zero Blue
    elif channel_name == 'B':
        channel[:,:,0] = 0  # Zero Red
        channel[:,:,1] = 0  # Zero Green
    else:
        print("Invalid channel")
        return
    
    plt.figure(figsize=(5,5))
    plt.imshow(channel)
    plt.title(f"{channel_name} Channel")
    plt.axis("off")
    plt.show()

# Show channels one by one
show_channel('R')
show_channel('G')
show_channel('B')