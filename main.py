import time
import pygetwindow as gw
import keyboard

# Find the Notepad window
notepad_window = gw.getWindowsWithTitle('Notepad')[0]

# Activate the Notepad window
notepad_window.activate()

# Set the keys to be typed
keys = input("")

# Type the keys into Notepad
for key in keys:
    keyboard.press(key)
    time.sleep(0.1)
    keyboard.release(key)
    time.sleep(0.1)

print("Typing completed.")
