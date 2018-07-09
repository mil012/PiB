"""
server.py

ECE196 Face Recognition Project
Author: Will Chen, Simon Fong

What this script should do:
1. Load a model with saved weights.
2. Create a webserver.
3. Handle classification requests:
    3.1 Save the image from the request.
    3.2 Load the image and classify it.
    3.3 Send the label and confidence back to requester(Pi).

Installation:
    pip install numpy keras tensorflow h5py flask flask-cors
"""
import cv2
import numpy as np
from keras.models import load_model
from flask import Flask, request, jsonify, abort, send_from_directory
from flask_cors import CORS

app = Flask(__name__)
CORS(app)                               # Allow CORS (Cross Origin Requests)

# TODO: Load the model from the weights file.
MODEL = #_______


def classify(path_to_image):
    """
    Classify a face image
    :param path_to_image: Path of face image
    :return: label and confidence in a dictionary
    """
    
    # Image dimensions that the model expects
    img_height, img_width, num_channel = 224, 224, 3
    
    # Used for VGG16 to normalize the images
    mean_pixel = np.array([104., 117., 123.]).reshape((1, 1, 3))

    # TODO: Use opencv to read and resize image to standard dimensions
    img = #______
    resized_img = #______
    
    # TODO: Subtract mean_pixel from the image store the new image in 
    # a variable called 'normalized_image'
    normalized_image = #________
    
    # Turns image shape of (2,) to (1,2)
    image_to_be_classified = np.expand_dims(normalized_image, axis=0)
    

    # TODO: Use network to predict the 'image_to_be_classified' and
    # get an array of prediction values
    # Note: MODEL.predict() returns an array of arrays ie. [[classes]]
    predictions = #______
    
    # TODO: Get the predicted label which is defined as follows:
    # Label = the index of the largest value in the prediction array
    # This label is a number, which corresponds to the same number you 
    # give to the folder when you organized data
    # Hint: np.argmax
    label = #________
    
    
    # TODO: Calculate confidence according to the following metric:
    # Confidence = prediction_value / sum(all_prediction_values)
    # Be sure to call your confidence value 'conf'
    # Hint: np.sum()
    label_value = #_______
    total = #_________
    conf = #__________

    
    prediction = {'label': str(label),
                  'confidence': float(conf)}

    return 

@app.route('/')
def index():
    """
    Handles sending the webcam tool.
    """
    return send_from_directory('.','index.html')

# Persons seen list. Contains prediction dictionaries of label and confidence.
persons = []

@app.route('/person/<person>')
def get_person(person):
    """ Handles returning persons last seen.

    If a integer is given, return the the person in that index of the array.
    If the string 'last', return the last person seen.
    If anything else, return an error.

    :param person: index | last | other
    :return: prediction | error
    """

    # Default prediction to return. If nobody has been logged yet.
    prediction = {'error': 'No body seen yet.'}

    # Default index
    index = None

    # Handle specific index
    try:
        index = int(person)

    except ValueError as e:
        print("Exception: {}".format(e))

    # Handle last person
    if(person == 'last'):
        index = -1
    
    # Handle out of bounds.
    try:
         prediction = persons[index]
    except IndexError as e:
        # When index is not in range.
        print("Exception: {}".format(e))
    except TypeError as e:
        # When index is None
        print("Exception: {}".format(e))

    # Converts python dictionary into JSON format
    prediction_json = jsonify(prediction)
    
    # Respond to the request (Send prediction back to Pi)    
    return prediction_json

@app.route('/predict')
def predict():
    """Receives an image, classifies the image, and responds with the label."""
    
    image = None
    
    # This extracts the image data from the request 
    if(request.method == 'POST'):
        if('image' not in request.form and 'image' not in request.json):
            print(request.form)
            abort(400)
        try:    
            image = request.json['image']
        except(TypeError):
            image = request.form['image']
        
    starter = image.find(',')
    image_data = image[starter+1:]
    
    # Path where the image will be saved
    temp_image_name = 'temp.jpg'
    
    # Decodes the image data and saves the image to disk                   
    with open(temp_image_name, 'wb') as fh:
        fh.write(image_data.decode('base64'))
    
    # TODO: Call classify to predict the image and save the result to a 
    # variable called 'prediction'
    prediction = classify(temp_image_name)

    # Add to persons list
    persons.append(prediction)
    
    # Converts python dictionary into JSON format
    prediction_json = jsonify(prediction)
    
    # Respond to the request (Send prediction back to Pi)    
    return prediction_json
        
def main(args):
    app.run(host='0.0.0.0', port=args.port, threaded=False, 
        debug=args.debug, ssl_context=args.ssl)


if(__name__ == "__main__"):
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('-p','--port', help="Port that the server will run on.", type=int, default=8080)
    parser.add_argument('-d','--debug', help="Whether or not to run in debug mode.", default=False, action='store_true')
    parser.add_argument('-s','--ssl', help="Whether or not to run with HTTPS", default='adhoc', action='store_const',const='adhoc')

    args = parser.parse_args()
    main(args)
