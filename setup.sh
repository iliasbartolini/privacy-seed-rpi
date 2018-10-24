#!/bin/sh

sudo apt-get install python3-serial python3-pip --yes
pip3 install pygame

sudo cp /home/pi/privacy-seed-rpi/privacy-seed.sh /etc/init.d/privacy-seed.sh

sudo update-rc.d privacy-seed.sh defaults
