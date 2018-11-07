from Crypto.PublicKey import ECC
from base64 import b64encode
from base64 import b64decode
from Crypto.Cipher import AES
import sys

'''
Program to encrypt or decrypt a file using ECC key generator and AES Cipher Feedback Mode algorithm.
'''

#command line functionality
#command line: python ./ecies.py e/d input.txt

mode = sys.argv[1]
file = sys.argv[2]

#get input from file as a string
with open(file, 'r') as myfile:
    input = myfile.read().replace('\n', ' ')

#convert input from string to bytes
data = bytes(input, 'utf-8')

#generate key using ECC library
key1 = ECC.generate(curve='P-256')

#print ECC key
print(key1)

#get private key in byte form
key = bytes(str(key1.d), 'utf-8')

#truncate to 16 bytes because AES-128 only accepts up to 16 bytes for a key
key = key[:16]

#initialize cipher and encrypt data (plaintext) to ciphertext
cipher = AES.new(key, AES.MODE_CFB)
ct_bytes = cipher.encrypt(data)
iv = b64encode(cipher.iv).decode('utf-8')
ct = b64encode(ct_bytes).decode('utf-8')

#decode iv and ct
decoded_iv = b64decode(iv)
decoded_ct = b64decode(ct)

#initialize cipher and decrypt ciphertext to plaintext
cipher = AES.new(key, AES.MODE_CFB, iv = decoded_iv)
pt = cipher.decrypt(decoded_ct)

#open output.txt to write mode
f = open("output.txt", "w")

#write either encrypted or decrypted text based on command line argument
if mode == 'e':

    #print encrypted text if mode is 'e'
    print("Encrypting file...")
    print("Encrypted text: ")
    print(ct)

    #write to file
    f.write("Encrypted Text: ")
    f.write(str(ct))

if mode == 'd':

    #print decrypted text if mode is 'd'
    print("Decrypting file...")
    print("Decrypted text: ")
    print(pt)

    #write to file
    f.write("Decrypted Text: ")
    f.write(str(pt))
