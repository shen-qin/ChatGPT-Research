import time
import random

def hammer(address):
    for i in range(100000):
        byte = random.randint(0, 255)
        mem.write(address, byte)

def test(address):
    original_value = mem.read(address)
    for i in range(1000):
        hammer(address)
    new_value = mem.read(address)
    return original_value != new_value

if __name__ == "__main__":
    mem = open("/dev/memfd", "rb+")
    address = 0x100000000
    if test(address):
        print("Rowhammer vulnerability detected!")
    else:
        print("No Rowhammer vulnerability detected.")