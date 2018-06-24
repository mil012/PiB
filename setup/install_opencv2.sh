cd ~
sudo apt-get install build-essential cmake git libgtk2.0-dev pkg-config libavcodec-dev
libavformat-dev libswscale-dev python-dev python-numpy libtbb2 libtbb-dev libjpeg-dev
libpng-dev libtiff-dev libjasper-dev libdc1394-22-dev

#Get files
wget -O opencv.zip https://github.com/opencv/opencv/archive/2.4.13.4.zip
unzip opencv.zip
cd ~/opencv-2.4.13.4
mkdir build
cd build
cmake -D CMAKE_BUILD_TYPE=Release -D CMAKE_INSTALL_PREFIX=/usr/local ..
make -j3
sudo make install
