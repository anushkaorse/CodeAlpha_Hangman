import os
import shutil

# Folder to organize
folder_path = "my_files"

# Folder where JPG images will be moved
images_folder = os.path.join(folder_path, "Images")

# Create Images folder if it does not exist
if not os.path.exists(images_folder):
    os.makedirs(images_folder)

# Check all files in the folder
for file_name in os.listdir(folder_path):

    # Check if the file is a JPG image
    if file_name.lower().endswith(".jpg"):

        source_path = os.path.join(folder_path, file_name)

        destination_path = os.path.join(images_folder, file_name)

        shutil.move(source_path, destination_path)

        print("Moved:", file_name)

print("\nJPG files have been organized successfully!")