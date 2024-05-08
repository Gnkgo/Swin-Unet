import os

def remove_last_char_from_filenames(directory):
    for filename in os.listdir(directory):
        if filename.endswith(".png"):
            # Remove the last character from the filename, not including the extension
            new_name = filename[:-5] + filename[-4:]
            # Full path for old and new names
            old_file = os.path.join(directory, filename)
            new_file = os.path.join(directory, new_name)
            # Rename the file
            os.rename(old_file, new_file)
            print(f"Renamed '{filename}' to '{new_name}'")

# Specify the directory containing the images
directory_path = 'datasets\scar'
remove_last_char_from_filenames(directory_path)
