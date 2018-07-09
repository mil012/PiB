#!/usr/bin/env python3
"""
svm_sklearn.py

Performs classification on the MNIST dataset using SVM.

Author: Simon Fong
"""

def _main(args):
    
    import numpy as np
    from sklearn.svm import SVC
    

    # Load dataset
    from keras.datasets import mnist
    (x_train, y_train), (x_test, y_test) = mnist.load_data()
    
    # Process images
    x_train = np.reshape(x_train,(60000,784))
    x_test = np.reshape(x_test,(10000,784))
    print("Reshaped x data into {}".format(x_train.shape))

    # Subset of training data to reduce training time.
    # NOTE: This is only 3000/60000. Training with the full set would take too long.
    SUBSET = 3000
    x_train = x_train[:SUBSET]
    y_train = y_train[:SUBSET]

    # Train with data.
    print("Begin fitting...")

    # TODO: Create an SVM with a cache_size=2048
    svm = #________

    # TODO: Fit the data
    # Hint: svm.fit
    #___________
    print("Classifier fitted.")

    # Evaluate on testing data.
    print("Begin predicting.")

    # TODO: Evaluate on testing data
    # Hint: svm.score
    acc = #___________
    print("Accuracy: {}".format(acc))



  
if(__name__ == '__main__'):
    import argparse
    parser = argparse.ArgumentParser()
    
    args = parser.parse_args()
    _main(args)