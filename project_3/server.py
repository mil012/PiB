"""
ECE196 Face Recognition Project
Author: Will Chen, Simon Fong

What this script should do:
1. Load a model with saved weights.
2. Create a webserver.
3. Handle classification requests:
    3.1 Save the image from the request.
    3.2 Load the image and classify it.
    3.3 Send the label and confidence back to requester(Pi).
"""
import cv2
import numpy as np
from keras.models import load_model
from flask import Flask, request, jsonify, g, abort, send_from_directory
from flask_cors import CORS

app = Flask(__name__)
CORS(app)                               # Allow CORS (Cross Origin Requests)

# TODO: Read saved weights
def get_model():
    """
    Retrieves and returns the model. Handles global with flask.
    :return: model
    """
    model = getattr(g, 'model', None)
    if model is None:
        model = g.model = # _________   # Load the model from weight file
    return model

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

    
    # TODO: Subtract mean_pixel from the image store the new image in 
    # a variable called 'normalized_image'
     
    
    # Turns image shape of (2,) to (1,2)
    image_to_be_classified = np.expand_dims(normalized_image, axis=0)
    
    # TODO: Get the model using
    model = #_____

    # TODO: Use network to predict the 'image_to_be_classified' and
    # get an array of prediction values
    # Note: model.predict() returns an array of arrays ie. [[classes]]
    
    
    # TODO: Get the predicted label which is defined as follows:
    # Label = the index of the largest value in the prediction array
    # This label is a number, which corresponds to the same number you 
    # give to the folder when you organized data
    # Hint: np.argmax
    
    
    # TODO: Calculate confidence according to the following metric:
    # Confidence = prediction_value / sum(all_prediction_values)
    # Be sure to call your confidence value 'conf'
    
    prediction = {'label': label,
                  'confidence': float(conf)}

    return prediction

@app.route('/predict')
def predict():
    """Receives an image, classifies the image, and responds with the label."""
    
    image = None
    
    # This extracts the image data from the request 
    if(request.method == 'POST'):
        
        if('image' not in request.form):
            print(request.form)
            abort(400)    
        image = request.form['image']
        data = {'data':'foo'}
        
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
    
    # Converts python dictionary into JSON format
    prediction_json = jsonify(prediction)
    
    # Respond to the request (Send prediction back to Pi)    
    return prediction_json
        
def main():
    # Starts the webserver
    app.run(host='0.0.0.0', port=8080, threaded=False, debug=True)

# Runs the main function if this file is run directly
if(__name__ == "__main__"):
    main()
