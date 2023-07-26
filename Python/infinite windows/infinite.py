import subprocess
import time

def open_finder_windows():
    while True:
       time.sleep(2)
       subprocess.call(['open', '-a', 'Finder'])

# Unleash the chaos!
open_finder_windows()
