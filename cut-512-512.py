from PIL import Image
import os

def crop_images(source_directory, target_directory):
    for filename in os.listdir(source_directory):
        if filename.endswith('.jpg') or filename.endswith('.png'):  # Process only jpg and png images
            file_path = os.path.join(source_directory, filename)

            with Image.open(file_path) as img:
                width, height = img.size

                # Ensure the image is large enough
                if width >= 512 and height >= 512:
                    # Crop the middle bottom
                    bottom_crop = img.crop((width // 2 - 256, height - 512, width // 2 + 256, height))
                    bottom_crop.save(os.path.join(target_directory, filename.replace('.', 'B.')))

                    # Crop the middle right
                    right_crop = img.crop((width - 512, height // 2 - 256, width, height // 2 + 256))
                    right_crop.save(os.path.join(target_directory, filename.replace('.', 'R.')))

# Usage
source_directory = '/Users/bengisu/Downloads/deneme'
target_directory = '/Users/bengisu/Downloads/deneme512'
crop_images(source_directory, target_directory)

