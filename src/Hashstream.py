import sys
import os
from Crypto.Hash import SHA256

def get_file_bytes(file_name, chunk_size):
    blocks = []
    fp = open(file_name, 'rb')

    chunk_bytes = fp.read(chunk_size)
    while chunk_bytes:
        blocks.append(chunk_bytes)
        chunk_bytes = fp.read(chunk_size)

    return blocks

def get_hash_from_bytes(chunk_bytes):
    last_hash = bytearray()
    while chunk_bytes:
        chunk = bytearray(chunk_bytes.pop())
        chunk += last_hash

        last_hash = bytearray(SHA256.new(data = chunk).digest())

    return last_hash

if __name__ == "__main__":

    args = sys.argv[1:]
    if(len(args) < 1):
        print('Usage: hashstream.py <file_name>')

    file_name = args[0]
    
    fbytes = get_file_bytes(file_name, 1024)
    h0 = get_hash_from_bytes(fbytes)
    print('Hash:', h0.hex())
