import time
import threading
import pygame
from pynput import keyboard

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

    octave = 4

    sound_keys = {
        "q": ['a',octave - 1],
        "w": ['a-',octave - 1],
        "e": ['b',octave - 1],
        "r": ['c',octave - 1],
        "t": ['c-',octave - 1],
        "z": ['d',octave - 1],
        "u": ['d-',octave - 1],
        "i": ['e',octave - 1],
        "o": ['f',octave - 1],
        "p": ['f-',octave - 1],
        "ü": ['g',octave - 1],
        "+": ['g-',octave - 1],
        "a": ['a',octave],
        "s": ['a-',octave],
        "d": ['b',octave],
        "f": ['c',octave],
        "g": ['c-',octave],
        "h": ['d',octave],
        "j": ['d-',octave],
        "k": ['e',octave],
        "l": ['f',octave],
        "ö": ['f-',octave],
        "ä": ['g',octave],
        "#": ['g-',octave],
        "<": ['a',octave + 1],
        "y": ['a-',octave + 1],
        "x": ['b',octave + 1],
        "c": ['c',octave + 1],
        "v": ['c-',octave + 1],
        "b": ['d',octave + 1],
        "n": ['d-',octave + 1],
        "m": ['e',octave + 1],
        ",": ['f',octave + 1],
        ".": ['f-',octave + 1],
        "-": ['g',octave + 1]#,
        #"-": ['g-',ocatave + 1],
    }

    try:

        sound_key = sound_keys[key.char]

        play_sound(sound_key[0],sound_key[1])

    except AttributeError:

        print('special key {0} pressed'.format(key))

def on_release(key):
    #print('{0} released'.format(key))
    if key == keyboard.Key.esc:
        # Stop listener
        return False

# Collect events until released
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()