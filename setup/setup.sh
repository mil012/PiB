#!/usr/bin/env bash

# Install various tools and perform environment setup for Raspberry Pi 3 for
# face recognition project by Project in a Box.
# Author: Simon Fong

# Notes:
# PiCamera: https://raspberrypi.stackexchange.com/questions/14229/how-can-i-enable-the-camera-without-using-raspi-config

# General system updates
sudo apt-get update -y
sudo apt-get upgrade -y

# Enable SSH
sudo systemctl enable ssh
sudo systemctl start ssh

# Install Vim for text editing
sudo apt-get install vim -y

# Set keyboard to US layout
sudo cp keyboard /etc/default/keyboard

# Enable PiCamera (Same from raspi-config)
CONFIG="/boot/config.txt"
if grep -Fxq "start_x=1" $CONFIG
then
    echo "Camera already enabled."
else
    if grep -Fxq "start_x=0" $CONFIG
    then
        echo "start_x=0 found. Enabling now..."
        sed -i 's/start_x=0/start_x=1/g' $CONFIG
    else
        echo "start_x not found. Appending now..."
        echo "start_x=1" >> $CONFIG
        echo "gpu_mem=128" >> $CONFIG
    fi
fi

# Install Python packages

# Install environment tool
sudo pip install virtualenv

# Install Flask and CORS
sudo pip install flask flask-cors

# Install Machine Learning Framework
# pip install tensorflow keras h5py


