#!/bin/sh

while [ 1 ]
do
  sudo ./python/privacy_seed.py /dev/ttyUSB1 /dev/ttyUSB2
  sleep 5
done
