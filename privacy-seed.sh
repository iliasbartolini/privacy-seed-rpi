#!/bin/sh
### BEGIN INIT INFO
# Provides:          privacy-seed
# Required-Start:    $remote_fs $syslog
# Required-Stop:     $remote_fs $syslog
# Default-Start:     3 4 5
# Default-Stop:      0 1 6
# Short-Description: Start daemon at boot time
# Description:       Enable service provided by daemon.
### END INIT INFO

sudo rm /var/log/privacy-seed.log
sudo touch /var/log/privacy-seed.log
sudo chmod 777 /var/log/privacy-seed.log

cd /home/pi/privacy-seed-rpi/
git pull -r

while [ 1 ]
do
  date >> /var/log/privacy-seed.log 2>&1
  sudo /home/pi/privacy-seed-rpi/python/privacy_seed.py /dev/ttyUSB0 /dev/ttyUSB1 >> /var/log/privacy-seed.log 2>&1
  sleep 5
done
