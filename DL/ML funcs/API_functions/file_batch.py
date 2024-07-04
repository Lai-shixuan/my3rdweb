import os
import glob
import cv2


# A date structure to include prefix, suffix and middle name:
class ImageName:
    def __init__(self, prefix, suffix):
        self.prefix = prefix
        self.suffix = suffix
        print(f"Your image name format is: {self.prefix}_XXXX{self.suffix}")


# A function to get all image in specific format, with prefix, and suffix:
def get_image_names(folder_path: str, my_image_names: ImageName, image_format: str):
    search_path = os.path.join(folder_path, my_image_names.prefix + '*' + my_image_names.suffix + '.' + image_format)
    image_files_names = glob.glob(search_path)

    # Test if there is any image in the folder:
    if not image_files_names:
        raise Exception('Error: No images found')

    # Some information about the images:
    print(f"{len(image_files_names)} images have been found in {folder_path}")
    if len(image_files_names) > 3:
        print("The first 3 images are:")
        for i in range(3):
            print(image_files_names[i])
    else:
        print("All images are:")
        for image_file in image_files_names:
            print(image_file)
    print(f"\033[1;3mGet names completely!\033[0m")
    return image_files_names


def read_images(image_files_names: list, color_style: str):
    if not image_files_names:
        raise Exception('Error: No images found')
    images = []
    if color_style == 'gray':
        for image_file in image_files_names:
            image = cv2.imread(image_file, cv2.IMREAD_GRAYSCALE)
            images.append(image)
    elif color_style == 'color':
        for image_file in image_files_names:
            image = cv2.imread(image_file)
            images.append(image)
    print(f"{len(images)} images have been read")
    print(f"\033[1;3mReading completely!\033[0m")
    return images


# A function to output all images to a specific folder in a specific format, with a specific name format:
def output_images(image_files, output_folder, my_image_name, output_format):
    if not image_files:
        raise Exception('Error: No images found')
    for idx, image_file in enumerate(image_files):
        new_file_name = f"{my_image_name.prefix}_{idx:04d}{my_image_name.suffix}.{output_format}"
        new_file_path = os.path.join(output_folder, new_file_name)
        cv2.imwrite(new_file_path, image_file)
    print(f"{len(image_files)} images have been saved to {output_folder} with the format {output_format}")
    print("\033[1;3mOutput completely!\033[0m")
