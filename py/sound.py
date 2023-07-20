import time
import threading
import platform
from pynput import keyboard

def play_sound(frequency):
    duration = 100  # milliseconds
    if platform.system() == 'Windows':
        import winsound
        winsound.Beep(frequency, duration)
    elif platform.system() == 'Linux':
        import subprocess
        subprocess.call(['play', '-n', 'synth', str(duration/1000), 'sin', str(frequency)])

def on_press(key):
    try:
        if key.char == 'a':
            play_sound(261)
        elif key.char == 's':
            play_sound(293)
        elif key.char == 'd':
            play_sound(329)
        elif key.char == 'f':
            play_sound(349)
        elif key.char == 'g':
            play_sound(392)
        elif key.char == 'h':
            play_sound(440)
        elif key.char == 'j':
            play_sound(493)
        elif key.char == 'k':
            play_sound(523)
        elif key.char == 'l':
            play_sound(587)
        elif key.char == 'ö':
            play_sound(659)
        elif key.char == 'ä':
            play_sound(698)
        elif key.char == '#':
            play_sound(784)
    except AttributeError:
        print('special key {0} pressed'.format(key))

def on_release(key):
    print('{0} released'.format(key))
    if key == keyboard.Key.esc:
        # Stop listener
        return False

# Collect events until released
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()