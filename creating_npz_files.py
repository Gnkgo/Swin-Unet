import os
from PIL import Image
import numpy as np

def png_to_npz(image_path, label_path, output_path):
    # Load image file
    img = Image.open(image_path).convert('L')  # Convert to grayscale
    img_np = np.array(img) / 255.0  # Normalize pixel values to [0, 1]

    # Load label file
    label = Image.open(label_path).convert('L')  # Assuming label is also a grayscale image
    label_np = np.array(label) / 255.0  # Normalize pixel values to [0, 1]

    # Save to .npz file
    np.savez(output_path, image=img_np, label=label_np)

def convert_folder_to_npz(image_dir, label_dir, output_dir):
    # Ensure output directory exists
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # List all PNG images in the image directory
    image_files = [f for f in os.listdir(image_dir) if f.endswith('.png')]
    
    for image_file in image_files:
        # Assuming label files have the same name as image files
        image_path = os.path.join(image_dir, image_file)
        #label_name = image_file.replace('_slice000', '')
        label_path = os.path.join(label_dir, image_file)
        
        if os.path.exists(label_path):  # Check if the corresponding label file exists
            # Define output path
            output_file = image_file.replace('.png', '.npz')
            output_path = os.path.join(output_dir, output_file)
            
            # Convert and save to .npz
            png_to_npz(image_path, label_path, output_path)
            print(f"Converted and saved: {output_file}")
        else:
            print(f"No corresponding label found for {image_file}")

# Example usage
convert_folder_to_npz('datasets/train_png', 'datasets/train_label_png', 'datasets/train_npz')
