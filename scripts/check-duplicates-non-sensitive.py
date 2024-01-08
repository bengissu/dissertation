# Query: 
# ContextLines: 1

import os
from skimage.io import imread
from skimage.color import rgb2gray
from skimage.transform import resize
import numpy as np

def load_images_from_directory(directory):
    images = []
    for filename in os.listdir(directory):
        if filename.endswith('.jpg') or filename.endswith('.png'):  # Add other file types if needed
            img_path = os.path.join(directory, filename)
            images.append(imread(img_path))
    return images

def resize_to_standard(image, size=(100, 100)):
    return resize(image, size)

def convert_to_grayscale(image):
    return rgb2gray(image)

def calculate_basic_features(image):
    # Example: Calculate the histogram
    histogram, _ = np.histogram(image, bins=256, range=(0, 1))
    return histogram / np.sum(histogram)  # Normalize the histogram

def euclidean_distance(feature1, feature2):
    return np.linalg.norm(feature1 - feature2)

def is_duplicate(feature1, feature2, threshold=0.1):
    return euclidean_distance(feature1, feature2) < threshold

def detect_duplicates(directory):
    images = load_images_from_directory(directory)
    resized_images = [resize_to_standard(image) for image in images]
    grayscale_images = [convert_to_grayscale(image) for image in resized_images]

    features = [calculate_basic_features(image) for image in grayscale_images]
    
    duplicates = []
    for i, img_feature in enumerate(features):
        for j, other_feature in enumerate(features):
            if i != j and is_duplicate(img_feature, other_feature):
                duplicates.append((i, j))
    
    return duplicates

# Example usage
directory = '/Users/bengisu/Downloads/deneme'
duplicate_pairs = detect_duplicates(directory)
print(duplicate_pairs)
