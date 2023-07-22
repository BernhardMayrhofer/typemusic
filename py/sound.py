import time
import threading
import platform
import pygame
from pynput import keyboard

channels = 10
channel = 1

pygame.mixer.init()
pygame.mixer.set_num_channels(channels)

def play_sound(note,octave):
    duration = 100  # milliseconds
    global channel

    if platform.system() == 'Windows':
        import winsound
        #winsound.Beep(frequency, duration)
    elif platform.system() == 'Linux':
        import subprocess
        #subprocess.call(['play', '-n', 'synth', str(duration/1000), 'sin', str(frequency)])

        try:
            #pygame.mixer.music.load("samples/" + note + str(octave) + "v9.wav")
            #pygame.mixer.music.play()
            pygame.mixer.Channel(channel).play(pygame.mixer.Sound("samples/" + note + str(octave) + ".mp3"))
            channel += 1
            if (channel >= channels):
                channel = 1
        except:
            print('Sample ' + note + str(octave) + "v9.wav not found")


def on_press(key):
    try:
        if key.char == 'a':
            play_sound('c',4)
        elif key.char == 's':
            play_sound('c-',4)
        elif key.char == 'd':
            play_sound('d',4)
        elif key.char == 'f':
            play_sound('d-',4)
        elif key.char == 'g':
            play_sound('e',4)
        elif key.char == 'h':
            play_sound('f',4)
        elif key.char == 'j':
            play_sound('f-',4)
        elif key.char == 'k':
            play_sound('g',4)
        elif key.char == 'l':
            play_sound('g-',4)
        elif key.char == 'ö':
            play_sound('a',5)
        elif key.char == 'ä':
            play_sound('a-',5)
        elif key.char == '#':
            play_sound('b',5)
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