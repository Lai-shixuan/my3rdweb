# use another package and it is much more efficiently

import os
import numpy as np
import cv2
import pyvista as pv
import configparser


def read_and_resize_images(folder, size, method_name, radius):
    img_files = sorted([os.path.join(folder, f) for f in os.listdir(folder)
                        if (f.endswith('.png') and method_name in f and f.startswith(str(radius)))])
    img_data = []

    side_length = int(size)

    i = 0

    for img_file in img_files:
        i = i+1
        if i > 20:
            break

        img = cv2.imread(img_file)
        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        if side_length != 0:
            img = cv2.resize(img, (side_length, side_length), interpolation=cv2.INTER_LINEAR)

        img_array = np.array(img) > 0
        img_data.append(img_array)

    img_tensor = np.array(img_data)
    img_tensor = ~img_tensor
    return img_tensor


def visualize_3d_tensor(tensor):
    # Create the spatial reference
    # tensor = tensor
    grid = pv.StructuredGrid(*np.mgrid[0:tensor.shape[0]:complex(tensor.shape[0]),
                              0:tensor.shape[1]:complex(tensor.shape[1]),
                              0:tensor.shape[2]:complex(tensor.shape[2])])

    # Set the grid scalars
    grid["values"] = tensor.flatten(order="F")

    # Threshold the grid to create a mesh
    mesh = grid.threshold(1)

    # Create a plotter object and set the scalars to the Z height
    plotter = pv.Plotter()
    plotter.add_mesh(mesh, scalars="values", show_edges=False, opacity=1)

    # Add a cube frame
    height = tensor.shape[0]
    width = tensor.shape[1]
    length = tensor.shape[2]
    bounds = (0, height, 0, width, 0, length)  # xMin, xMax, yMin, yMax, zMin, zMax
    cube = pv.Box(bounds=bounds, level=0)
    plotter.add_mesh(cube, style='wireframe', color='blue')
    plotter.show_axes()

    # Display the plotter
    plotter.show()

    # 使用 PyVista 从点云创建一个多面体网格
    points = np.argwhere(tensor)
    cloud = pv.PolyData(points)


def index_calculating(tensor):
    index_list = []
    sum_true = np.sum(tensor)
    sum_all = tensor.shape[0] * tensor.shape[1] * tensor.shape[2]
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
