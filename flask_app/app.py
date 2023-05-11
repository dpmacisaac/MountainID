from flask import Flask, render_template, request
import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import datetime
import random
import string

model = load_model('tl_model_v5.h5')
app = Flask(__name__, static_folder='static')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    img_file = request.files['image']

    # Generate a unique filename
    timestamp = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
    random_string = ''.join(random.choices(string.ascii_lowercase + string.digits, k=8))
    filename = f'{timestamp}_{random_string}.jpg'

    img_path = './static/' + filename
    img_file.save(img_path)
    img = image.load_img(img_path, target_size=(224, 224))
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    pred = model.predict(img_array)
    class_names = ['K2', 'Kangchenjunga', 'Mauna Kea', 'Mt Denali', 'Mt Everest', 'Mt Fitz Roy', 'Mt Fuji', 'Mt Hood', 'Mt Kilimanjaro', 'Mt Rainier', 'Mt Whitney']
    predicted_class = class_names[np.argmax(pred)]
    # Render the prediction.html template with the mountain name and percentage
    confidence = pred[0][class_names.index(predicted_class)]
    is_predicted = True
    if confidence < 0.5:
        is_predicted = False
        
    return render_template('prediction.html', is_predicted=is_predicted, name=predicted_class, percent=round(confidence*100,2),  image_file=filename)

@app.route('/process')
def process():
    return render_template('process.html')

@app.route('/about_me')
def about_me():
    return render_template('about_me.html')

@app.route('/stats')
def stats():
    return render_template('stats.html')

if __name__ == '__main__':
    app.run(debug=True)
