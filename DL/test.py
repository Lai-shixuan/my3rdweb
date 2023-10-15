#%%
import torch
import numpy as np
import pandas
from PIL import Image, ImageFilter
import matplotlib

#%%
torch.cuda.is_available()

print(np.random.random([1, 2]))

print(torch.cuda.is_available())
print(torch.cuda.current_device())
print(torch.cuda.get_device_name(0))
print(torch.cuda.device_count())

print(torch.__version__)

#%%
im1 = Image.open(r"../image/download24.jpg")
im1.show()
im2 = im1.filter(ImageFilter.MedianFilter(size=9))
im2.show()
