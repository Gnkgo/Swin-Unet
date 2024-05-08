import os
import shutil

# Source folder containing .png files
source_folder = 'lists\lists_scar'

# Destination folder where .png files will be moved
destination_folder = 'lists\lists_scarpng'

# Ensure the destination folder exists, if not, create it
if not os.path.exists(destination_folder):
    os.makedirs(destination_folder)

# Get a list of all files in the source folder
files = os.listdir(source_folder)

# Iterate through each file
for file in files:
    # Check if the file is a .png file
    if file.endswith('.png'):
        # Construct the full path of the source file
        source_file = os.path.join(source_folder, file)
        # Construct the full path of the destination file
        destination_file = os.path.join(destination_folder, file)
        # Move the file to the destination folder
        shutil.move(source_file, destination_file)
