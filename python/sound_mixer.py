#!/usr/bin/env python3

import subprocess
import pygame
from pprint import pprint


class SoundMixer:

    def __init__(self):
        pygame.init()
        self.pin_sound = pygame.mixer.Sound('media/pin.wav')
        self.water_droplet_sound = pygame.mixer.Sound('media/water_droplet.wav')

    def play_pin(self):
        self.pin_sound.play(-1)

    def play_water_droplet(self):
        self.water_droplet_sound.play(-1)
