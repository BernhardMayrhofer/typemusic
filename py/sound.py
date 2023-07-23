import time
import threading
import pygame
from pynput import keyboard

import json
data = json.load(open('py/config.json'))

octave = data["octave"]

channels = 10
channel = 1

pygame.mixer.init()
pygame.mixer.set_num_channels(channels)

def play_sound(note,octave):
    duration = 100  # milliseconds
    global channel

    import subprocess
    try:
        pygame.mixer.Channel(channel).play(pygame.mixer.Sound("samples/" + note + str(octave) + ".mp3"))
        channel += 1
        if (channel >= channels):
            channel = 1
    except:
        print('Sample ' + note + str(octave) + "v9.wav not found")


def on_press(key):
    
    #midi_key 61 = A4

    try:

        sound_key = data["sound_keys"][key.char]

        play_sound(sound_key[0],octave + sound_key[1])

    except AttributeError:

        print('special key {0} pressed'.format(key))

def on_release(key):
    #print('{0} released'.format(key))
    if key == keyboard.Key.esc:
        # Stop listener
        return False

# Collect events until released
#with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
#    listener.join()