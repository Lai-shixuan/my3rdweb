import open3d as o3d
import numpy as np

# Sample data
np.random.seed(0)
points = np.random.rand(100, 3)  # 100 random 3D points

# Create an Open3D PointCloud object
pcd = o3d.geometry.PointCloud()
pcd.points = o3d.utility.Vector3dVector(points)

# Estimate normals
pcd.estimate_normals(search_param=o3d.geometry.KDTreeSearchParamHybrid(radius=0.1, max_nn=30))

# Ball Pivoting algorithm to create a mesh
radii = [0.005, 0.01, 0.02, 0.04]
mesh = o3d.geometry.TriangleMesh.create_from_point_cloud_ball_pivoting(pcd, o3d.utility.DoubleVector(radii))

# Visualize the mesh
o3d.visualization.draw_geometries([mesh])
