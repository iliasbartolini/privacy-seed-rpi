# Privacy Seed RPI

Raspberry PI installation notes and custom script for the Privacy Seed


## Base image setup

Download and Install raspbian Pi image

https://www.raspberrypi.org/downloads/raspbian/

https://www.raspberrypi.org/documentation/installation/installing-images/linux.md

### Lite
```
wget https://downloads.raspberrypi.org/raspbian_latest -O raspbian-latest.zip
unzip raspbian-latest.zip
sudo dd bs=4M if=2018-06-27-raspbian-stretch.img of=/dev/sda conv=fsync
sync
```

### Full/GUI
```
wget https://downloads.raspberrypi.org/raspbian_lite_latest -O raspbian-lite-latest.zip
unzip raspbian-lite-latest.zip
sudo dd bs=4M if=2018-06-27-raspbian-stretch-lite.img of=/dev/sda conv=fsync
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

sudo apt-get install unattended-upgrades --yes
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

### Testing the speaker (no alsa needed)
```
wget http://rpf.io/lamp3 -O small_example.mp3 --no-check-certificate
wget 'http://soundbible.com/grab.php?id=2162&type=wav' -O heartbeat.wav

sudo apt-get install omxplayer --yes
omxplayer -o local small_example.mp3
omxplayer -o local heartbeat.wav

```

###

//sudo apt-get install alsa-utils mpg123 --yes

### Bluetooth speaker
// sudo apt-get install bluetooth bluez blueman

- try pulseaudio
- try bluez


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
