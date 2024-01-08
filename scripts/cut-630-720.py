from PIL import Image
import os

def crop_center(image_path, output_path, new_width, new_height):
    with Image.open(image_path) as img:
        left = (img.width - new_width) / 2
        top = (img.height - new_height) / 2
        right = (img.width + new_width) / 2
        bottom = (img.height + new_height) / 2

        cropped_image = img.crop((left, top, right, bottom))
        cropped_image.save(output_path)

def crop_images_in_directory(source_directory, target_directory, new_width, new_height):
    for filename in os.listdir(source_directory):
        if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.tiff', '.bmp', '.gif')):
            image_path = os.path.join(source_directory, filename)
            output_path = os.path.join(target_directory, filename)
            crop_center(image_path, output_path, new_width, new_height)



source_directory = '/Users/bengisu/Downloads/bk277-welshdata/images/images'
target_directory = '/Users/bengisu/Downloads/deneme'
crop_images_in_directory(source_directory, target_directory, 630, 720)

