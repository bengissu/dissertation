import os
import hashlib

def file_hash(filepath):
    """Generate a hash for a file."""
    with open(filepath, 'rb') as f:
        return hashlib.md5(f.read()).hexdigest()

def find_duplicate_images(search_path):
    """Find duplicates of the first image of each participant in the specified search path."""
    duplicates = {}
    
    # Iterate over participant numbers
    for participant in range(2, 21):  # Assuming participants numbered from 02 to 20
        target_image_name = f"participant_{str(participant).zfill(2)}_set_01_frame000.png"
        target_image_path = os.path.join(search_path, target_image_name)
        if not os.path.exists(target_image_path):
            print(f"Target image {target_image_name} not found.")
            continue

        target_hash = file_hash(target_image_path)
        duplicates[target_image_name] = 0

        # Compare with other images
        for root, dirs, files in os.walk(search_path):
            for file in files:
                if file.endswith('.png') and file != target_image_name:
                    path = os.path.join(root, file)
                    if file_hash(path) == target_hash:
                        duplicates[target_image_name] += 1

    return duplicates

# Example usage
search_directory = '/path/dissertation/welshdata/images-630-720'  # Replace with the directory to search in

duplicate_counts = find_duplicate_images(search_directory)
for image, count in duplicate_counts.items():
    print(f'Number of duplicates for {image}: {count}')
