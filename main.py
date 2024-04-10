#!/usr/bin/python3
import os
import time
import config
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame
import random

def playsound(sound_file):
    if config.nagsfx:
        pygame.mixer.init()
        pygame.mixer.music.load(sound_file)
        pygame.mixer.music.play()
        return True
    return False

failattempt = 0

while True:
    time.sleep(config.delay)

    if os.system("ping -c 1 " + config.host + " &> /dev/null ") == 0:
        if failattempt > 0:
            print(f"up after {failattempt}")
            failattempt = 0
            i = random.randint(1, 3)
            playsound(f"sfx/up{i}.mp3")
        continue

    if config.nagmsg:
        os.system("echo \"SERVER IS DOWN!\" > /dev/pts/0")
    failattempt += 1
    print(f"down attempt {failattempt} fail")

    if failattempt < 6:
        playsound(f"sfx/attempt{failattempt}.mp3")
    else:
        i = random.randint(1, 4)
        playsound(f"sfx/random{i}.mp3")
