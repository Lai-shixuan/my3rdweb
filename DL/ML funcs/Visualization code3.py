# it works, 3D scatter by GPT4
import os
import open3d as o3d
import numpy as np
from PIL import Image

def read_and_resize_images(img_folder, resize_dims):
    """
    Read images from a folder, resize them and convert them into a 3D tensor.

    Parameters:
    img_folder (str): Path to the folder containing images.
    resize_dims (tuple): The dimensions to resize the images to.

    Returns:
    3D numpy array: A 3D tensor representation of the images.
    """
    # Get a sorted list of all image files in the folder
    img_files = sorted([os.path.join(img_folder, f) for f in os.listdir(img_folder) if f.endswith('.png') or f.endswith('.jpg')])

    # Initialize an empty list to store the image data
    img_data = []

    # Loop through all image files
    for img_file in img_files:
        # Open the image file
        img = Image.open(img_file)

        # Resize the image
        img = img.resize(resize_dims, Image.BICUBIC)

        # Convert the image data to a binary format (True if the pixel is not purely black, False otherwise)
        img_array = np.array(img.convert('L')) > 0

        # Add the image data to the list
        img_data.append(img_array)

    # Convert the list of image data to a 3D numpy array
    img_tensor = np.array(img_data)

    return img_tensor

def visualize_3d_tensor(tensor):
    """
    Visualize a 3D tensor as a 3D image.

    Parameters:
    tensor (3D numpy array): The 3D tensor to visualize.
    """
    # Convert the 3D tensor to a point cloud
    pcd = o3d.geometry.PointCloud()
    pcd.points = o3d.utility.Vector3dVector(np.transpose(tensor.nonzero()))

    pcd.paint_uniform_color([1, 0, 0])  # Red color for points
    o3d.visualization.RenderOption.point_size = 1000  # Adjust point size here

    # Visualize the point cloud
    o3d.visualization.draw_geometries([pcd])

# Define your image folder and resize dimensions here
img_folder = "d:/9-mysitewin/DL/ML funcs/data/result/"
resize_dims = (100, 100)

# Read and resize the images
tensor = read_and_resize_images(img_folder, resize_dims)

# Visualize the 3D tensor
visualize_3d_tensor(tensor)