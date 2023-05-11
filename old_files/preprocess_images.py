import os
import json
import requests
import cv2
import flickrapi
import shutil
import numpy as np

MOUNTAINS = ['Mt Whitney', 'Mt Hood', 'Mt Borah','Mt Rainier', 'Mt Everest']
SIZE = (224,224)

def preprocess_image(image_path, image_size):
    # Load the image from the given image path
    image = cv2.imread(image_path)
    # Resize the image to the desired size
    image = cv2.resize(image, image_size)
    # Convert the image to grayscale
    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # Apply histogram equalization to improve contrast
    image = cv2.equalizeHist(image)
    # Convert the image to a float and normalize pixel values to [0, 1]
    image = image.astype(np.float32) / 255.0
    # Add an extra dimension to represent a batch of size 1
    image = np.expand_dims(image, axis=0)
    # Return the preprocessed image
    return image


if __name__ == '__main__':
    # Create a new folder to store the preprocessed images
    for mountain in MOUNTAINS:
        folder_path = 'images/'+ mountain
        processed_folder_path = 'processed_images/' + mountain
        os.makedirs(processed_folder_path, exist_ok=True)

        # Loop through all files in the folder
        for file_name in os.listdir(folder_path):
            # Get the full path to the image file
            image_path = os.path.join(folder_path, file_name)
            # Preprocess the image using the preprocess_image function
            preprocessed_image = preprocess_image(image_path, SIZE)
            # Save the preprocessed image to the new folder
            processed_image_path = os.path.join(processed_folder_path, file_name)
            cv2.imwrite(processed_image_path, preprocessed_image[0] * 255)