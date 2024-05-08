import os

folder_path = "datasets/train_label_png"

# Iterate through all files in the folder
for filename in os.listdir(folder_path):
    if filename.endswith(".png"):
        # Split the filename into base and extension
        base, ext = os.path.splitext(filename)
        
        # Get the parts before and after " + slice"
        
        parts = base.split("_")
        if len(parts) > 1 and "mastectomy" in parts[0]:
            new_filename = f"case0{parts[1]}_slice000.png"
            
            # Construct the full file paths
            old_filepath = os.path.join(folder_path, filename)
            new_filepath = os.path.join(folder_path, new_filename)
            
            # Rename the file
            os.rename(old_filepath, new_filepath)
            print(f"Renamed {filename} to {new_filename}")
