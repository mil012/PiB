#!/usr/bin/env bash

# Script to install OpenCV on Raspberry Pi 3
# Information from Will Chen and this website:
# https://www.pyimagesearch.com/2017/09/04/raspbian-stretch-install-opencv-3-python-on-your-raspberry-pi/
# Author: Simon Fong

# Install everything in home directory.
cd /home/pi

# Developer tools used in build process
sudo apt-get install build-essential cmake pkg-config git -y

# Image I/O libraries
sudo apt-get install libjpeg-dev libtiff-dev libjasper-dev libpng-dev -y

# Video I/O libraries
sudo apt-get install libavcodec-dev libavformat-dev libswscale-dev -y

# GUI libraries
sudo apt-get install libgtk2.0-dev -y

# Threaded, not sure
sudo apt-get install libtbb2 libtbb-dev -y
   
# Cameras I/O
sudo apt-get install libdc1394-22-dev -y
   
# Python and Numpy
sudo apt-get install python-dev python-numpy -y

#Get files
wget -O opencv.zip https://github.com/opencv/opencv/archive/2.4.13.4.zip
unzip opencv.zip
cd /home/pi/opencv-2.4.13.4
mkdir build
cd build
cmake -D CMAKE_BUILD_TYPE=Release -D CMAKE_INSTALL_PREFIX=/usr/local ..
make -j3            # May take up to 2 hours.
sudo make install
