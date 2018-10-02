"""
test_cnn.py

Tests the cnn on the test set of MNIST.

ECE196 Face Recognition Project
Author: Will Chen, Simon Fong
"""
from keras.models import load_model
from keras.datasets import mnist
from keras.utils import to_categorical
import keras
import numpy as np
import cv2

# Proccess the data from (28,28) to (32,32)
def procces_image(img):
    proccesed_image = cv2.resize(img, (32,32))
    return proccesed_image

# Process and shape datasets
def get_dataset():
    # Load MNIST dataset.
    (x_train, y_train), (x_test, y_test) = mnist.load_data()

    # Resize the images by applying the function to all the images.
    x_train = np.array(map(procces_image, x_train))
    x_test = np.array(map(procces_image, x_test))

    # Reshape to fit model
    x_train = np.reshape(x_train,(60000,32,32,1))
    x_test = np.reshape(x_test,(10000,32,32,1))
    print("Resized images to {}".format(x_train.shape))

    # One hot encode labels.
    y_train = to_categorical(y_train)
    y_test = to_categorical(y_test)

    # Reshape to fit model
    y_train = np.reshape(y_train,(60000,1,1,10))
    y_test = np.reshape(y_test,(10000,1,1,10))

    return (x_train, y_train), (x_test, y_test)

def _main(args):
    # Load MNIST dataset.
    (x_train, y_train), (x_test, y_test) = get_dataset()

    # TODO: Load the model from your file. It should be 'yann_mnist.h5'
    # Hint: Use load_model import above.
    model = #_________

    BATCH_SIZE = 16

    # TODO: Test the model using x_test, y_test, and batch size
    # Hint: model.evaluate
    metrics = #___________
    
    # Print out the accuracy.
    print("{metrics_names[0]}: {metrics[0]} \n {metrics_names[1]}: {metrics[1]}".format(metrics=metrics, 
        metrics_names=model.metrics_names))

if(__name__ == '__main__'):
    import argparse
    parser = argparse.ArgumentParser()
    
    args = parser.parse_args()
    _main(args)
