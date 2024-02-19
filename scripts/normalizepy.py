import os
from PIL import Image
import numpy as np

def normalize_image(image_path, output_path):
    """
    Normalize the pixel values of an image to the range [0, 1] and save it to output_path.
    """
    with Image.open(image_path) as img:
        img_array = np.array(img).astype(np.float32) / 255.0
        normalized_img = Image.fromarray(np.uint8(img_array * 255))
        normalized_img.save(output_path)

def normalize_all_images(input_directory, output_directory):
    """
    Normalize all images in the input_directory and save them to output_directory.
    """
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    for filename in os.listdir(input_directory):
        if filename.lower().endswith(('.png', '.jpg', '.jpeg')):
            input_path = os.path.join(input_directory, filename)
            output_path = os.path.join(output_directory, filename)
            normalize_image(input_path, output_path)

# Replace these paths with your actual directories
input_directory = '/path/to/your/input/images'
output_directory = '/path/to/your/output/images'

normalize_all_images(input_directory, output_directory)
print("All images have been normalized and saved to the output directory.")
