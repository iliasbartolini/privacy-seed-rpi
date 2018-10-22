#!/bin/sh

while [ 1 ]
do
  sudo /home/pi/privacy-seed-rpi/python/privacy_seed.py /dev/ttyUSB0 /dev/ttyUSB1
  sleep 5
done
