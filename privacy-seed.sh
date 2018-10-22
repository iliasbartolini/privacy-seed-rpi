#!/bin/sh

sudo touch /var/log/privacy-seed.log
sudo chmod 777 /var/log/privacy-seed.log

while [ 1 ]
do
  date >> /var/log/privacy-seed.log 2>&1
  sudo /home/pi/privacy-seed-rpi/python/privacy_seed.py /dev/ttyUSB0 /dev/ttyUSB1 >> /var/log/privacy-seed.log 2>&1
  sleep 5
done
