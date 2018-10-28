#!/usr/bin/env python3

import subprocess
import pygame
from pprint import pprint


class SoundMixer:

    def __init__(self):
        pygame.init()
        self.pin_sound = pygame.mixer.Sound('media/pin.wav')
        self.water_droplet_sound = pygame.mixer.Sound('media/water_droplet.wav')
        self.water_droplet_sound.set_volume(.8)
        self.heartbeat_sound = pygame.mixer.Sound('media/heartbeat.wav')
        self.base_sound = pygame.mixer.Sound('media/base.ogg')
        self.base_sound.set_volume(.4)

    def play_pin_loop(self):
        self.pin_sound.play(-1)

    def play_water_droplet_loop(self):
        self.water_droplet_sound.play(-1)

    def play_heartbeat_loop(self):
        self.heartbeat_sound.play(-1)

    def play_heartbeat(self):
        self.heartbeat_sound.play()

    def play_base(self):
        self.base_sound.play(-1)
