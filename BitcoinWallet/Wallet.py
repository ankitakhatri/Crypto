from Crypto.PublicKey import RSA

def newKeyPair():
    #function to generate a new key pair
    key = RSA.generate(1024)
    f = open("private.pem", "wb")
    f.write(key.exportKey('PEM'))
    f.close()

    pubkey = key.publickey()
    f = open("public.pem", "wb")
    f.write(pubkey.exportKey('OpenSSH'))
    f.close()

# def list():
# 	#function to list all the public private key pairs
# 	#print them by name
#
# def display(key):
# 	#function to display a specific key
# 	#planning to use QR code
#
# def base58Check():
# 	#function to encode a base58 address
# 	#code for this: https://github.com/bitcoin/bitcoin/blob/master/src/base58.h