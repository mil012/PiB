# Install various tools and perform environment setup for Raspberry Pi 3 for
# face recognition project by Project in a Box.
# Author: Simon Fong

# General system updates
sudo apt-get update -y
sudo apt-get upgrade -y

# Enable SSH (Does not seem t work)
sudo systemctl enable ssh
sudo systemctl start ssh

# Install Vim for text editing
sudo apt-get install vim -y

# Set keyboard to US layout
sudo cp keyboard /etc/default/keyboard


