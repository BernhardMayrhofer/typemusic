from pynput import keyboard

import sound
import midi_text

with keyboard.Listener(on_press=sound.on_press, on_release=sound.on_release) as listener:
    listener.join()
