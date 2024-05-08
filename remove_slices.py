def modify_file(input_file, output_file):
    with open(input_file, 'r') as file:
        lines = file.readlines()
    
    # Process each line to remove '_slice000'
    modified_lines = [line.replace('_slice000', '') for line in lines]

    with open(output_file, 'w') as file:
        file.writelines(modified_lines)

# Usage
input_filename = 'lists/lists_scar/test_vol.txt'  # This should be the name of your input file
output_filename = 'lists/lists_scar/test_vol.txt'  # This can be the same as input_filename if you want to overwrite the original file
modify_file(input_filename, output_filename)
