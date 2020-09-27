from Crypto.Hash import SHA256
sha256 = SHA256.new()

stream = open('SHA1.mp4', 'rb').read()

byte_stream = zip(*[iter(stream)]*1024)
print(byte_stream)

