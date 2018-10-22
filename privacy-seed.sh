#!/bin/sh

while [ 1 ]
do
  sudo ./python/privacy_seed.py /dev/ttyUSB0 /dev/ttyUSB1
  sleep 5
done
