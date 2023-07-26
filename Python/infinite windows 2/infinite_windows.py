import subprocess

while True:
    subprocess.run(['osascript', '-e', 'tell application "Google Chrome" to make new window'])
