#idea of how to generate a private key using import secrets
#requires python 3.6 or higher to use secrets module
#need to figure out a way to store them

import secrets

#generate bits
bits = secrets.randbits(256)
#convert to hex
bits_hex = hex(bits)
#store private key in hex form
private_key = bits_hex[2:]
