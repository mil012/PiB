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
set_config_var start_x 1 /boot/config.txt
CUR_GPU_MEM=$(get_config_var gpu_mem /boot/config.txt)
if [ -z "$CUR_GPU_MEM" ] || [ "$CUR_GPU_MEM" -lt 128 ]; then
  set_config_var gpu_mem 128 /boot/config.txt
fi
sed /boot/config.txt -i -e "s/^startx/#startx/"
sed /boot/config.txt -i -e "s/^fixup_file/#fixup_file/"


