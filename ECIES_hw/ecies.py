from Crypto.PublicKey import ECC
from base64 import b64encode
from base64 import b64decode
from Crypto.Cipher import AES
import sys

#command line functionality
#command line: python ./ecies.py e/d input.txt

mode = sys.argv[1]
file = sys.argv[2]

#get input from file as a string
with open(file, 'r') as myfile:
    input = myfile.read().replace('\n', ' ')

#generate key using ECC library
key1 = ECC.generate(curve='P-256')

data = bytes(input, 'utf-8')

#get private key in byte form
key = bytes(str(key1.d), 'utf-8')
key = key[:16]

#initialize cipher and encrypt data (plaintext) to ciphertext
cipher = AES.new(key, AES.MODE_CFB)
ct_bytes = cipher.encrypt(data)
iv = b64encode(cipher.iv).decode('utf-8')
ct = b64encode(ct_bytes).decode('utf-8')

#decode iv and ct
old_iv = b64decode(iv)
old_ct = b64decode(ct)
#initialize cipher and decrypt ciphertext to plaintext
cipher = AES.new(key, AES.MODE_CFB, iv = old_iv)
pt = cipher.decrypt(old_ct)

#write to file ouput.txt
f = open("output.txt", "w")

if mode == 'e':

    #print encrypted text if mode is 'e'
    print("Encrypting file...")
    print("Encrypted text: ")
    print(ct)
    f.write("Encrypted Text: ")
    f.write(str(ct))

if mode == 'd':

    #print decrypted text is mode is 'd'
    print("Decrypting file...")
    print("Decrypted text: ")
    #print decrypted text
    print(pt)
    f.write("Decrypted Text: ")
    f.write(str(pt))
