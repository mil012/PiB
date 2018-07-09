#!/usr/bin/env python3
"""
train_face_recognizer.py

Trains a face recognizer.

Author: Simon Fong
"""

def is_opencv_2():
    ver = cv2.__version__
    num = int(ver.split('.')[0])
    return num == 2

import cv2
import os
import numpy as np

def detect_face(img):
    """ Crops the face from an image."""

    """ From: https://github.com/informramiz/opencv-face-recognition-python"""
    #convert the test image to gray image as opencv face detector expects gray images
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    #load OpenCV face detector, I am using LBP which is fast
    #there is also a more accurate but slow Haar classifier

    CASCADE_PATH = '../haarcascades/haarcascade_frontalface_default.xml'
    face_cascade = cv2.CascadeClassifier(CASCADE_PATH)

    #let's detect multiscale (some images may be closer to camera than others) images
    #result is a list of faces
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.2, minNeighbors=5);
    
    #if no faces are detected then return original img
    if (len(faces) == 0):
        return None, None
    
    #under the assumption that there will be only one face,
    #extract the face area
    (x, y, w, h) = faces[0]
    
    #return only the face part of the image
    return gray[y:y+w, x:x+h], faces[0]

def draw_rectangle(img, rect):
    (x, y, w, h) = rect
    cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)
    

def draw_text(img, text, x, y):
    cv2.putText(img, text, (x, y), cv2.FONT_HERSHEY_PLAIN, 1.5, (0, 255, 0), 2)


def predict(recognizer,test_img):
    """ Predict who it is based on an image"""
    #make a copy of the image as we don't want to chang original image
    img = test_img.copy()
    #detect face from the image
    face, rect = detect_face(img)

    if(rect is None):
        return test_img

    # TODO: Resize image to (100,100)
    face = # _______

    # TODO: Predict the image using our face recognizer 
    # Hint: use recognizer.predict and face
    label, confidence = # ________
    

    #get name of respective label returned by face recognizer
    #label_text = subjects[label]
    
    #draw a rectangle around face detected
    draw_rectangle(img, rect)
    #draw name of predicted person
    draw_text(img, str(label), rect[0], rect[1]-5)
    
    return img

def train(data_dir):
    face_recognizer = None

    # Handle OpenCV 2
    if(is_opencv_2()):
        face_recognizer = cv2.createLBPHFaceRecognizer()
    # Handle OpenCV 3
    else:
        face_recognizer = cv2.face.LBPHFaceRecognizer_create()


    images =[]
    labels = []

    person_dirs = os.listdir(data_dir)
    
    # Reads in all the face images and uses directory name as the label.
    for index,person_dir in enumerate(person_dirs):
        print("Training on {}".format(person_dir))
        
        person_dir_path = os.path.join(data_dir,person_dir)
        for image_path in os.listdir(person_dir_path):
            
            image_path = os.path.join(person_dir_path,image_path)
            image  = cv2.imread(image_path)
            image = cv2.resize(image, (100,100))
            gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            images.append(gray)
            labels.append(int(person_dir))

    # TODO: Train the face_recognizer using images and np.array(labels)
    #__________

    print("Finished training.")

    return face_recognizer

def predict_live(recognizer):


    print("Starting live feed.")
    # TODO: Get video feed from camera and store it in frame and in a loop
    # for
        frame = #________
        predicted_image = predict(recognizer, frame)
        cv2.imshow('Face', predicted_image)
        # Wait one second and exit if 'q' is pressed.
        key = cv2.waitKey(1) & 0xFF
        if key == ord("q"):
            break

def _main(args):
    # TODO: Specify the directory of your images
    DATA_DIR = ''
    recognizer = train(DATA_DIR)
    predict_live(recognizer)
  
if(__name__ == '__main__'):
    import argparse
    parser = argparse.ArgumentParser()
    args = parser.parse_args()
    _main(args)