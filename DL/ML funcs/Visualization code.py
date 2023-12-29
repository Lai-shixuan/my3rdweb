# use another package and it is much more efficiently

import os
import numpy as np
from PIL import Image
import pyvista as pv
import configparser
import math


def read_and_resize_images(folder, size, method_name, ROI):
    img_files = sorted([os.path.join(folder, f) for f in os.listdir(folder)
                        if (f.endswith('.png') and method_name in f and str(ROI) in f)])
    img_data = []

    for img_file in img_files:
        img = Image.open(img_file)
        # if size != '(0, 0)':
            # img = img.resize(size, Image.BICUBIC)

        # Create a new image with a black background
        background = Image.new('RGBA', img.size, (0, 0, 0, 255))

        # Paste the original image onto the background
        background.paste(img, mask=img.split()[3])  # 3 is the alpha channel

        # Convert back to grayscale (L mode) while keeping the black background
        background = background.convert('L')

        img_array = np.array(background) > 0
        img_data.append(img_array)

    img_tensor = np.array(img_data)
    return img_tensor


def visualize_3d_tensor(tensor):
    # Create the spatial reference
    grid = pv.StructuredGrid(*np.mgrid[0:tensor.shape[0]:complex(tensor.shape[0]),
                              0:tensor.shape[1]:complex(tensor.shape[1]),
                              0:tensor.shape[2]:complex(tensor.shape[2])])

    # Set the grid scalars
    grid["values"] = tensor.flatten(order="F")

    # Threshold the grid to create a mesh
    mesh = grid.threshold(1)

    # Create a plotter object and set the scalars to the Z height
    plotter = pv.Plotter()
    plotter.add_mesh(mesh, show_edges=False, opacity=1)

    # Add a cylindrical frame
    radius = max(tensor.shape[1], tensor.shape[2]) / 2
    height = tensor.shape[0]
    cylinder = pv.Cylinder(center=(height / 2, radius, radius), radius=radius, height=height, direction=(1, 0, 0))
    plotter.add_mesh(cylinder, style='wireframe', color='blue')

    # Display the plotter
    plotter.show()

    # 使用 PyVista 从点云创建一个多面体网格
    points = np.argwhere(tensor)
    cloud = pv.PolyData(points)


def index_calculating(tensor):
    index_list = []
    sum_true = np.sum(tensor)
    sum_all = tensor.shape[0] * tensor.shape[1] * tensor.shape[2] * math.pi / 4
    bulk_density = sum_true / sum_all
    index_list.append(bulk_density)
    return index_list


config = configparser.ConfigParser()
config.read('config.ini')
output_path = config['DEFAULT']['output_path']
resize_dims = config['DEFAULT']['resize_dims']
method_name = config['DEFAULT']['method_name']
ROI = int(config['DEFAULT']['ROI'])

images = read_and_resize_images(output_path, resize_dims, method_name, ROI)
index = index_calculating(images)
print(index)
visualize_3d_tensor(images)
