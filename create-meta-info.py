import os

def write_file_paths_to_txt(directory, output_file):
    """
    Writes the paths of files in the given directory to the specified output text file.

    :param directory: Path of the directory whose file paths are to be written.
    :param output_file: Path of the output text file.
    """
    with open(output_file, 'w') as file:
        for root, dirs, files in os.walk(directory):
            for name in files:
                # Construct the relative path of each file
                file_path = os.path.join(root, name)
                # Write the relative path to the output file
                file.write(file_path + '\n')

# Example usage
directory = 'path/welshdata'
output_file = 'images-metainfo.txt'


write_file_paths_to_txt(directory, output_file)
