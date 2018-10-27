# Privacy Seed RPI

Raspberry PI installation notes and custom integration script.
This component is part of the [https://privacy-seed.org/](Privacy Seed) project.

## TODO

- Slow shoutdown: process kill not handled
- Logrotate


## Base image setup

Download and Install raspbian Pi image

https://www.raspberrypi.org/downloads/raspbian/

https://www.raspberrypi.org/documentation/installation/installing-images/linux.md

### Lite
```
wget https://downloads.raspberrypi.org/raspbian_latest -O raspbian-latest.zip
unzip raspbian-latest.zip
sudo dd bs=4M if=2018-06-27-raspbian-stretch.img of=/dev/sda conv=fsync  status=progress
sync
```

### Full/GUI
```
wget https://downloads.raspberrypi.org/raspbian_lite_latest -O raspbian-lite-latest.zip
unzip raspbian-lite-latest.zip
sudo dd bs=4M if=2018-06-27-raspbian-stretch-lite.img of=/dev/sda conv=fsync  status=progress
sync
```

### Basic config

change password
```
passwd
```

```
sudo raspi-config
```
  - hostname -> privacy-seed
  - network -> connect to wifi
  - interfacing -> enable ssh


### Basic config for Full/GUI (currently testing for simplifying Bluetooth speaker)

  - follow wizard
  - change hostname, sshd, config wifi
  - `bluetoothctl`
    - `scan on`
    - `connect AA:BB:CC:DD:FF`
  - install vlc/mplayer


### User ssh key
Whatever IP address you get from dhcp... eg.
```
export PI_IP_ADDRESS=192.168.1.207
export PI_IP_ADDRESS=192.168.2.172

ssh-copy-id pi@$PI_IP_ADDRESS
```

### Upgrade

```
sudo apt-get update
sudo apt-get upgrade

## not for pi-seed
## sudo apt-get install unattended-upgrades --yes
```

### Custom user login (optional)

```
sudo apt-get install fortune fortunes cowsay finger --yes

echo '
if [ -x /usr/games/fortune ] ; then
    echo
    /usr/games/fortune | cowsay -W 90 -T '\'' U'\''
    echo
fi

echo '\'''\''
last -n 10
echo '\'''\''
finger
echo '\'''\''
uptime
' >> ~/.profile
```

## Audio tools (work in progress)

```
sudo apt-get install alsa-utils mpg123 --yes
alsamixer
```
  => Increase volume to ~90%

### Testing the speaker (no alsa needed)

```
wget http://rpf.io/lamp3 -O small_example.mp3 --no-check-certificate
wget 'http://soundbible.com/grab.php?id=2162&type=wav' -O heartbeat.wav
wget 'http://soundbible.com/grab.php?id=1073&type=wav' -O pin.wav
wget 'http://soundbible.com/grab.php?id=6&type=wav' -O ambient_cave.wav
wget 'http://soundbible.com/grab.php?id=384&type=wav' -O water_droplet.wav

sudo apt-get install omxplayer --yes
omxplayer -o local small_example.mp3
omxplayer -o local heartbeat.wav


sudo apt-get install mplayer --yes
```


### Bluetooth speaker

sudo apt-get install bluetooth bluez blueman --yes
lsusb | grep Bluetooth | cut -d' ' -f6

sudo btmon

sudo apt-get install pulseaudio-module-bluetooth --yes
pulseaudio -k
pulseaudio --start  
  ?? sudo ??

sudo pactl load-module module-bluetooth-discover
> /etc/pulse/default.pa
#module-bluetooth-policy
#module-bluez5-device
#module-bluez5-discover

lsusb | grep Bluetooth | cut -d' ' -f6

hciconfig

sudo bluetoothctl -a
select 5C:F3:70:8D:C6:D7
devices
power on
agent on
default-agent
scan on
-
scan off
trust XX:XX:XX:XX:XX:XX
pair XX:XX:XX:XX:XX:XX
connect XX:XX:XX:XX:XX:XX
quit

?? sudo vi /etc/systemd/system/bluetooth.service.d/a2dp.conf
?? sudo vi /etc/systemd/system/bluetooth.target.wants/bluetooth.service
ExecStart=/usr/lib/bluetooth/bluetoothd --plugin=a2dp
# ?? sudo systemctl restart bluetooth
?? systemctl daemon-reload



### Stuttering and audio interruptions
# If a low-power machine stutters (audio breaks up), you can try adding the following to /etc/pulse/daemon.conf:
high-priority = no
nice-level = -1
realtime-scheduling = yes
realtime-priority = 5
flat-volumes = no
resample-method = speex-float-1
default-sample-rate = 48000


# Privacy seed integration (work in progress)

```
sudo apt-get install git --yes
git clone https://github.com/iliasbartolini/privacy-seed-rpi.git
cd privacy-seed-rpi
./setup.sh
./privacy-seed.sh
```

## RNG tools

`sudo apt-get install rng-tools --yes`

### Check entropy available
`watch -n 1 cat /proc/sys/kernel/random/entropy_avail`

### Flush entropy by dumping /dev/random
`hexdump /dev/random`


# Deprecated parts

## I2C Setup (deprecated - not necessary anymore)

```
sudo apt-get install python-dev python-rpi.gpio --yes
sudo apt-get install i2c-tools --yes
sudo apt-get install python-smbus --yes
```
`sudo raspi-config`  > interfacing > I2C

Testing I2C devices

`sudo i2cdetect -y 1`


## Using pigpio module (deprecated - not necessary anymore)

```
sudo apt-get install python3-pigpio -d

sudo systemctl enable pigpiod
sudo systemctl start pigpiod
```
