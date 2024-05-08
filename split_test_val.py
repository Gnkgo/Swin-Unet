import os

def list_filenames_without_extension(folder_path, output_file):
    with open(output_file, 'w') as f:
        for filename in os.listdir(folder_path):
            #remove the extension from the filename
            filename = os.path.splitext(filename)[0]
            f.write(filename + '\n')

# Replace 'folder_path' with the path to your folder containing the PNG files
folder_path = 'data/Scar/train_npz'
# Replace 'output.txt' with the desired name of the output text file
output_file = 'lists/lists_Scar/train.txt'

list_filenames_without_extension(folder_path, output_file)
