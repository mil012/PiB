#!/usr/bin/env python3
"""
visualizer.py

Visualize image data.

Author: Simon Fong
"""
import cv2


def _main(args):
    import sys
    from keras.datasets import mnist
    (x_train, y_train), (x_test, y_test) = mnist.load_data()

    count = 10

    for i in range(count):

        # TODO: Access the i'th image in x_train
        # Hint: x_train[0] is the 0'th element
        img = #_________


        label = str(y_train[i])

        # TODO: Use imshow to display the images
        #__________

        # This is required for the image to show up and 
        # it waits for a key to be pressed to continue
        cv2.waitKey()
    
    
if(__name__ == '__main__'):
    import argparse
    parser = argparse.ArgumentParser()

    args = parser.parse_args()
    _main(args)