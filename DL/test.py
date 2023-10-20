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


#%%
#import numpy as np
import torch
import os
import torch.nn as nn
import torchvision.transforms as transforms
from PIL import Image
# "ConcatDataset" and "Subset" are possibly useful when doing semi-supervised learning.
from torch.utils.data import ConcatDataset, DataLoader, Subset, Dataset
from torchvision.datasets import DatasetFolder, VisionDataset

# This is for the progress bar.
from tqdm.auto import tqdm
import random
#%%
myseed = 6666  # set a random seed for reproducibility
torch.backends.cudnn.deterministic = True
torch.backends.cudnn.benchmark = False
np.random.seed(myseed)
torch.manual_seed(myseed)
if torch.cuda.is_available():
    torch.cuda.manual_seed_all(myseed)