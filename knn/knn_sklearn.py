#!/usr/bin/env python3
"""
knn_sklearn.py

Performs K nearest neighbors on some given data. Uses sklearn's KNN.

Author: Simon Fong
"""

def _main(args):
    
    import numpy as np
    from sklearn.neighbors import KNeighborsClassifier

    # Load dataset
    from keras.datasets import mnist
    (x_train, y_train), (x_test, y_test) = mnist.load_data()
    
    # Proccess dataset
    x_train = np.reshape(x_train,(60000,784))
    x_test = np.reshape(x_test,(10000,784))
    print("Reshaped x data into {}".format(x_train.shape))

    # TODO: Create KNeighorsClassifier with neighbors 3, and n_jobs=-1
    knn = # ________

    # Train with data.
    print("Begin fitting...")

    # TODO: Fit the data
    # Hint: knn.fit
    # __________
    print("Classifier fitted.")

    # Evaluate on testing data.
    print("Begin predicting.")

    # TODO: Evaluate on testing data
    # Hint: knn.score
    acc = #_________
    print("Accuracy: {}".format(acc))

  
if(__name__ == '__main__'):
    import argparse
    parser = argparse.ArgumentParser()
    
    args = parser.parse_args()
    _main(args)