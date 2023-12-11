% Define desired cuboid dimensions
desired_width = 256;
desired_height = 256;
depth = 100;

% Create 3D cuboid tensor
cuboid = zeros(desired_width, desired_height, depth, 'logical');

% Define the directory containing 2D images
image_dir = 'path/to/images';

% Read and process 2D images
image_files = dir(fullfile(image_dir,'*.tif'));
for i = 1:length(image_files)
    % Read the image
    image = imread(fullfile(image_files(i).folder, image_files(i).name));
    
    % Convert the image to grayscale and resize
    image = rgb2gray(image);
    image = imresize(image, [desired_width, desired_height]);
    
    % Convert to logical and stack into the cuboid
    logical_image = logical(image);
    cuboid = cat(3, cuboid, logical_image);
end

% Create a blank 3D image
painted_cuboid = zeros(desired_width, desired_height, depth, 'uint8');

% Iterate through each 2D slice and paint based on truth value
for i = 1:size(cuboid, 3)
    painted_cuboid(:,:,i) = im2uint8(cuboid(:,:,i)) * 255;
end

% Display the 3D image using isosurface
[x,y,z] = meshgrid(1:size(painted_cuboid,1), 1:size(painted_cuboid,2), 1:size(painted_cuboid,3));
p = patch(isosurface(x,y,z,painted_cuboid,0.5));
isonormals(x,y,z,painted_cuboid,p);
set(p, 'FaceColor', 'interp', 'EdgeColor', 'none');
xlabel('X');
ylabel('Y');
zlabel('Z');
title('3D Visualization');
