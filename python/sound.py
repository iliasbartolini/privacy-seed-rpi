#!/usr/bin/env python3

import time
import subprocess
import pygame
from pprint import pprint

pygame.init()

# heartbeat_sound = pygame.mixer.Sound('media/heartbeat.wav')
pin_sound = pygame.mixer.Sound('media/pin.wav')
water_droplet_sound = pygame.mixer.Sound('media/water_droplet.wav')

# def play_heartbeat():
#     heartbeat_sound.play(-1)

def play_pin():
    pin_sound.play(-1)

def play_water_droplet():
    water_droplet_sound.play(-1)

play_pin()
time.sleep(.74234)
play_water_droplet()
time.sleep(.251)
play_pin()
time.sleep(5)
