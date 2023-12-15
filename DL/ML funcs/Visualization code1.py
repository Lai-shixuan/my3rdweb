# use another package and it is much more efficiently

import os
import numpy as np
from PIL import Image
import pyvista as pv

def read_and_resize_images(img_folder, resize_dims):
    img_files = sorted([os.path.join(img_folder, f) for f in os.listdir(img_folder) if f.endswith('.png') or f.endswith('.png')])
    img_data = []

    for img_file in img_files:
        img = Image.open(img_file)
        img = img.resize(resize_dims, Image.BICUBIC)
        img_array = np.array(img.convert('L')) > 0
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
    plotter.add_mesh(mesh, color="lightblue", show_edges=False, opacity=1)

    # Display the plotter
    plotter.show()

img_folder = "d:/9-mysitewin/DL/ML funcs/data/result/"
resize_dims = (100, 100)

tensor = read_and_resize_images(img_folder, resize_dims)
print(1)
visualize_3d_tensor(tensor)