import cv2
import numpy as np
import os
import argparse
import random
import logging


def reduce_snr(img, noise_level=30):
    """
    Reduces the signal-to-noise ratio of a color MRI image using OpenCV.

    Args:
    - image_path (str): Path to the MRI image file (PNG format).
    - noise_level (int): Level of Gaussian noise to add.

    Returns:
    - ndarray: The MRI image array with reduced SNR.
    """

    # Generate Gaussian noise for each color channel
    noise = np.random.normal(0, noise_level, img.shape)

    # Add noise to the image
    noisy_img = img + noise

    # Clip values to maintain pixel value range
    noisy_img = np.clip(noisy_img, 0, 255)

    return noisy_img



def add_ghosting_artifact(image, intensity=5, direction=(1, 0)):
    """
    Add a ghosting artifact to an image.

    Parameters:
    image (numpy.ndarray): The original image.
    intensity (int): The intensity of the ghosting effect.
    direction (tuple): The direction of the ghosting as (dx, dy).

    Returns:
    numpy.ndarray: The image with the ghosting artifact.
    """
    ghosted_image = image.copy()

    # Create a shifted version of the image
    M = np.float32([[1, 0, direction[0] * intensity], [0, 1, direction[1] * intensity]])
    shifted_image = cv2.warpAffine(image, M, (image.shape[1], image.shape[0]))

    # Blend the original and the shifted images
    cv2.addWeighted(ghosted_image, 0.5, shifted_image, 0.5, 0, ghosted_image)

    return ghosted_image


def add_susceptibility_artifact(image, area):
    """
    Add a simulated susceptibility artifact to a specified area of an image.

    Parameters:
    image (numpy.ndarray): The original image.
    area (tuple): A tuple of (x, y, width, height) specifying the area for the artifact.

    Returns:
    numpy.ndarray: The image with the simulated artifact.
    """

    x, y, width, height = area
    artifact_area = image[y:y+height, x:x+width]

    # Simulate distortion by applying a darkening effect
    # Adjust the intensity for a more realistic effect
    artifact_area = cv2.multiply(artifact_area, np.array([0.5]))  # Darken the area

    # Apply the artifact to the original image
    image[y:y+height, x:x+width] = artifact_area
    return image


def add_motion_artifact(image, area, direction=(0, 1), magnitude=10):
    """
    Add a simulated motion artifact to a specified area of an image.

    Parameters:
    image (numpy.ndarray): The original image.
    area (tuple): A tuple of (x, y, width, height) specifying the area for the artifact.
    direction (tuple): The direction of motion as (dx, dy).
    magnitude (int): The magnitude of the motion.

    Returns:
    numpy.ndarray: The image with the simulated artifact.
    """
    x, y, width, height = area
    artifact_area = image[y:y+height, x:x+width]

    # Create motion blur kernel
    kernel_size = magnitude
    kernel = np.zeros((kernel_size, kernel_size))
    dx, dy = direction
    kernel[(kernel_size - 1) // 2,:] = np.ones(kernel_size)  # Horizontal line
    kernel = cv2.warpAffine(kernel, cv2.getRotationMatrix2D((kernel_size / 2 -0.5, kernel_size / 2 -0.5), np.arctan2(dy, dx) * 180 / np.pi, 1.0), (kernel_size, kernel_size))
    kernel = kernel / kernel_size

    # Apply motion blur to the specified area
    artifact_area = cv2.filter2D(artifact_area, -1, kernel)

    # Apply the artifact to the original image
    image[y:y+height, x:x+width] = artifact_area
    return image


def reduce_spatial_resolution(image, reduction_factor=0.25):
    """
    Reduce the spatial resolution of an image.

    Parameters:
    image (numpy.ndarray): The original image.
    reduction_factor (float): The factor by which the image's resolution is reduced.

    Returns:
    numpy.ndarray: The resolution-reduced image.
    """

    # Resize down (reduce resolution)
    low_res_image = cv2.resize(image, (128,128), interpolation=cv2.INTER_LINEAR)

    return low_res_image



def add_gibbs_artifacts(image):
    """
    Add simulated Truncation (Gibbs) Artifacts to an image.

    Parameters:
    image (numpy.ndarray): The original image.

    Returns:
    numpy.ndarray: The image with simulated Gibbs artifacts.
    """
    # Apply a high-pass filter to simulate Gibbs ringing
    kernel = np.array([[-1, -1, -1],
                       [-1,  8, -1],
                       [-1, -1, -1]])
    high_pass = cv2.filter2D(image, -1, kernel)

    # Add the high-pass filtered image back to the original image to simulate ringing
    gibbs_artifact_image = cv2.addWeighted(image, 1, high_pass, 0.1, 0)

    return gibbs_artifact_image




def process_directory(source_directory, target_directory):
    """
    Process all images in the source directory, apply a random combination of 
    artifacts, and save them in the target directory. Log each action.
    """
    if not os.path.exists(target_directory):
        os.makedirs(target_directory)

    for filename in os.listdir(source_directory):
        if filename.lower().endswith(('.png', '.jpg', '.jpeg')):
            img_path = os.path.join(source_directory, filename)
            image = cv2.imread(img_path)

            if image is not None and image.shape[0] == 512 and image.shape[1] == 512:
                # Define the area for the artifact based on file name
                random_area = random.randint(150, 512)
                area = (512 - random_area, 512 - random_area, random_area, random_area)

                # Apply artifacts
                random_artifact = random.randint(1, 6)
                artifact_name = ""
                if random_artifact == 1:
                    image = add_susceptibility_artifact(image, area)
                    artifact_name = "susceptibility"
                elif random_artifact == 2:
                    image = add_motion_artifact(image, area)
                    artifact_name = "motion"
                elif random_artifact == 3:
                    image = add_ghosting_artifact(image)
                    artifact_name = "ghosting"
                elif random_artifact == 4:
                    image = add_gibbs_artifacts(image)
                    artifact_name = "Gibbs"
                elif random_artifact == 5:
                    image = reduce_snr(image)
                    artifact_name="low-SNR"
                else:
                    artifact_name = "NO"
                    pass
                
                # Make 1/4 resolution
                processed_image = reduce_spatial_resolution(image)
                
                # Save the processed image
                save_path = os.path.join(target_directory, filename)
                cv2.imwrite(save_path, processed_image)

                # Log the action
                logging.info(f"Processed {filename} with {artifact_name} artifact")

                print(f"Processed and saved: {filename}")
            else:
                logging.warning(f"Skipped or failed to read: {filename}")
                print(f"Skipped or failed to read: {filename}")



def main():
    # Argument parsing with named arguments
    parser = argparse.ArgumentParser(description='Process images')
    parser.add_argument('--path_lq', type=str, required=True, help='Path to the target directory containing high-quality images.')
    parser.add_argument('--path_hq', type=str, required=True, help='Path to the source directory to save low-quality images.')
    parser.add_argument('--path_log', default='artifacts.log', type=str, required=True, help='Path and name of the log file.')

    args = parser.parse_args()

    # Set up logging
def process_directory(source_directory, target_directory):
    """
    Process all images in the source directory, apply a random combination of 
    artifacts, and save them in the target directory. Log each action.
    """
    if not os.path.exists(target_directory):
        os.makedirs(target_directory)

    for filename in os.listdir(source_directory):
        if filename.lower().endswith(('.png', '.jpg', '.jpeg')):
            img_path = os.path.join(source_directory, filename)
            image = cv2.imread(img_path)

            if image is not None and image.shape[0] == 512 and image.shape[1] == 512:
                # Define the area for the artifact based on file name
                random_area = random.randint(150, 512)
                area = (512 - random_area, 512 - random_area, random_area, random_area)

                # Apply artifacts
                random_artifact = random.randint(1, 6)
                artifact_name = ""
                if random_artifact == 1:
                    image = add_susceptibility_artifact(image, area)
                    artifact_name = "susceptibility"
                elif random_artifact == 2:
                    image = add_motion_artifact(image, area)
                    artifact_name = "motion"
                elif random_artifact == 3:
                    image = add_ghosting_artifact(image)
                    artifact_name = "ghosting"
                elif random_artifact == 4:
                    image = add_gibbs_artifacts(image)
                    artifact_name = "Gibbs"
                elif random_artifact == 5:
                    image = reduce_snr(image)
                    artifact_name="low-SNR"
                else:
                    artifact_name = "NO"
                    pass
                
                # Make 1/4 resolution
                processed_image = reduce_spatial_resolution(image)
                
                # Save the processed image
                save_path = os.path.join(target_directory, filename)
                cv2.imwrite(save_path, processed_image)

                # Log the action
                logging.info(f"Processed {filename} with {artifact_name} artifact, random area: {random_area}")

                print(f"Processed and saved: {filename}")
            else:
                logging.warning(f"Skipped or failed to read: {filename}")
                print(f"Skipped or failed to read: {filename}")



def main():
    # Argument parsing with named arguments
    parser = argparse.ArgumentParser(description='Process images')
    parser.add_argument('--path_hq', type=str, required=True, help='Path to the source directory containing high-quality images.')
    parser.add_argument('--path_lq', type=str, required=True, help='Path to the target directory to save low-quality images.')
    parser.add_argument('--path_log', default='artifacts.log', type=str, required=False, help='Path and name of the log file.')

    args = parser.parse_args()

    # Set up logging
    logging.basicConfig(filename=args.path_log, level=logging.INFO, format='%(asctime)s - %(message)s')

    # Process images in the specified directory
    process_directory(args.path_hq, args.path_lq)
    print('Processing complete.')

if __name__ == '__main__':
    main()



