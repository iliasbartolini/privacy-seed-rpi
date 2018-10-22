#!/bin/sh

sudo apt-get install python3-serial --yes

sudo ln -s /home/pi/privacy-seed-rpi/privacy-seed.sh /etc/init.d/privacy-seed.sh

sudo update-rc.d privacy-seed.sh defaults
