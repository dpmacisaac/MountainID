import os
import json
import requests
import cv2
import flickrapi
import shutil
import numpy as np
import tensorflow as tf
from tensorflow.keras.applications.resnet50 import ResNet50
from tensorflow.keras.preprocessing import image
from tensorflow.keras.applications.resnet50 import preprocess_input, decode_predictions



MOUNTAINS = ['Mt Whitney', 'Mt Hood','Mt Rainier', 'Mt Everest', 'Mt Denali', 'K2', 'Mt Fuji', 'Mt Kilimanjaro','Mauna Kea', 'Mt Fitz Roy', 'Kangchenjunga']
COUNT = 100

def contains_mountain(image_path, model):
    # Load the image and preprocess it for the ResNet50 model
    img = image.load_img(image_path, target_size=(224, 224))
    x = image.img_to_array(img)
    x = np.expand_dims(x, axis=0)
    x = preprocess_input(x)

    # Use the model to predict the object in the image
    preds = model.predict(x)

    # Check if the top prediction is "mountain" with at least 75% confidence
    top_preds = decode_predictions(preds, top=15)[0]
    for pred in top_preds:
        if pred[1] == 'alp' or pred[1] == 'mountain' or pred[1] == 'cliff' or pred[1] == 'mountain range' or pred[1] == 'rock face':
            return True

    # If the image does not contain a mountain, move it to a new directory
    new_directory = 'deleted_images/'
    if not os.path.exists(new_directory):
        os.makedirs(new_directory)
    filename = os.path.basename(image_path)
    new_path = os.path.join(new_directory, filename)
    os.rename(image_path, new_path)
    """
    print("no mountain")
    for pred in top_preds:
        print(pred[1])
        print(pred[2])
    """
    return False


def detect_person(image_path):
    # Load the image using OpenCV
    img = cv2.imread(image_path)

    # Load the pre-trained Haar cascades for face and body detection
    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    body_cascade = cv2.CascadeClassifier('haarcascade_fullbody.xml')

    # Convert the image to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Detect faces and bodies in the image
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)
    bodies = body_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)

    # Check if any faces or bodies were detected
    if len(faces) > 0 or len(bodies) > 0:
        os.rename(image_path, '../deleted_images/' + image_path)
        print("Person detected and image deleted")
        return True
    return False


def flickr_search_dl(search_term, flickr_key,flickr_secret, amount_of_pics, page, model):
    flickr = flickrapi.FlickrAPI(flickr_key, flickr_secret, format='parsed-json')

    # Set your search parameters

    term = search_term + " landscape"
    search_params = {
        'text': term,
        'sort': 'relevance',
        'media': 'photos',
        'per_page': amount_of_pics,
        'page': page
    }

    # Make the API request
    try:
        response = flickr.photos.search(**search_params)

            # Extract photo information from response
        photos = response['photos']['photo']

        # Create 'images' folder if it doesn't exist
        if not os.path.exists('mtn_images/'+search_term):
            os.makedirs('mtn_images/' + search_term)

        # Download each photo in the response
        pic_count = 0
        for photo in photos:
            photo_url = f'https://live.staticflickr.com/{photo["server"]}/{photo["id"]}_{photo["secret"]}.jpg'
            r = requests.get(photo_url)
            path = f'mtn_images/{search_term}/{photo["id"]}.jpg'
            with open(path, 'wb') as f:
                f.write(r.content)
            if contains_mountain(path, model) == True:
                pic_count += 1
        # Update last downloaded page in text file
    except:
        pass

    return pic_count


if __name__ == '__main__':
    model = ResNet50(weights='imagenet')
    with open('secret/keys.json') as f:
        keys = json.load(f)
        flickr_key = keys['flickr_key']
        flickr_secret = keys['flickr_secret']
        # Increment page number for next search

    # Load saved page numbers from a file
    try:
        with open('src/last_pages.json') as f:
            last_pages = json.load(f)
    except FileNotFoundError:
        last_pages = {}

    for mountain in MOUNTAINS:
        # Get the last downloaded page for this mountain
        last_page = last_pages.get(mountain, 0)

        # Download the next page of photos for this mountain
        page = last_page + 1
        print('Downloading | page ' + str(page) + ' | ' + mountain)
        pic_count = flickr_search_dl(mountain, flickr_key, flickr_secret, COUNT, page, model=model)
        print("| downloaded " + str(pic_count) + " images")

        # Update the last downloaded page for this mountain
        last_pages[mountain] = page

    # Save the updated page numbers to a file
    with open('src/last_pages.json', 'w') as f:
        json.dump(last_pages, f)
    