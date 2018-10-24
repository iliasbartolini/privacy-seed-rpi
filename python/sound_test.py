#!/usr/bin/env python3

import time
import sys
sys.path.insert(0, "./python")
from sound_mixer import SoundMixer

sound_mixer = SoundMixer()
sound_mixer.play_base()

time.sleep(10)

sound_mixer.play_water_droplet()

time.sleep(30)
