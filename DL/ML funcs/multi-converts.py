import cv2
import os
import glob


# Function to convert BMP images to PNG format
def convert_bmp_to_png(folder_path):
    search_path = os.path.join(folder_path, '*.bmp')
    bmp_files = glob.glob(search_path)

    for idx, bmp_file in enumerate(bmp_files):
        image = cv2.imread(bmp_file, cv2.IMREAD_GRAYSCALE)
        new_file_name = f"1_png_{idx:03d}.png"
        new_file_path = os.path.join(folder_path, new_file_name)
        cv2.imwrite(new_file_path, image)


# Function to convert images to binary format
def convert_to_binary(folder_path):
    search_path = os.path.join(folder_path, '*.png')
    png_files = glob.glob(search_path)

    for idx, png_file in enumerate(png_files):
        image = cv2.imread(png_file, cv2.IMREAD_GRAYSCALE)
        if image is not None:
            binary_image = image // 255
            new_file_name = f"2_binary_{idx:03d}.png"
            new_file_path = os.path.join(folder_path, new_file_name)
            cv2.imwrite(new_file_path, binary_image)
        else:
            print(f"Image not found: {png_file}")


# Function to convert binary images to grayscale
def binary_to_grayscale(folder_path):
    search_path = os.path.join(folder_path, '*.png')
    binary_files = glob.glob(search_path)

    for idx, binary_file in enumerate(binary_files):
        image = cv2.imread(binary_file, cv2.IMREAD_GRAYSCALE)
        if image is not None:
            grayscale_image = image * 255
            new_file_name = f"3_grayscale_{idx:03d}.png"
            new_file_path = os.path.join(folder_path, new_file_name)
            cv2.imwrite(new_file_path, grayscale_image)
        else:
            print(f"Image not found: {binary_file}")


# Main function to select and run a specific conversion
def main():
    # folder_path = 'd:/15_Datas_in_papers/7_nnUNet/nnUNet_raw/Dataset002_test200/imagesTr/0118/'
    folder_path = 'd:/15_Datas_in_papers/temp/result/'
    print(f"This is your input output directory: {folder_path}")

    print("Select the operation:")
    print("1: Convert BMP to PNG")
    print("2: Convert to Binary")
    print("3: Convert Binary to Grayscale")

    choice = input("Enter your choice (1/2/3): ")

    if choice == '1':
        convert_bmp_to_png(folder_path)
    elif choice == '2':
        convert_to_binary(folder_path)
    elif choice == '3':
        binary_to_grayscale(folder_path)
    else:
        print("Invalid choice!")


if __name__ == "__main__":
    main()
