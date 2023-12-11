# it works perfectly but it is slow when no resizing the image

import numpy as np
from PIL import Image
import open3d as o3d
import os

def read_and_resize_images(image_folder, target_size):
    images = []
    for filename in sorted(os.listdir(image_folder)):
        if filename.endswith('.jpg'):  # Assuming images are in PNG format
            img = Image.open(os.path.join(image_folder, filename))
            img_resized = img.resize(target_size, Image.BICUBIC)
            images.append(np.asarray(img_resized))
    return np.stack(images, axis=-1)  # Creates a 3D tensor

def create_binary_tensor(tensor):
    # Convert to binary tensor. This is a placeholder; you'll need to define the logic
    # binary_tensor = tensor > 127  # Example threshold
    return tensor

def tensor_to_mesh(binary_tensor):
    # Convert binary tensor to a mesh.
    mesh = o3d.geometry.TriangleMesh()

    for i in range(binary_tensor.shape[0]):
        for j in range(binary_tensor.shape[1]):
            for k in range(binary_tensor.shape[2]):
                if binary_tensor[i, j, k]:
                    # Create a cube for each True value
                    cube = o3d.geometry.TriangleMesh.create_box(width=1, height=1, depth=1)
                    cube.translate([i, j, k])
                    mesh += cube

    mesh.compute_vertex_normals()
    return mesh

def visualize_mesh(mesh):
    o3d.visualization.draw_geometries([mesh])

# Example usage
image_folder = "d:/9-mysitewin/DL/ML funcs/data/result/"
tensor = read_and_resize_images(image_folder, (300, 300))  # Resize to 100x100
binary_tensor = create_binary_tensor(tensor)
mesh = tensor_to_mesh(binary_tensor)
visualize_mesh(mesh)
