from Crypto.PublicKey import ECC
import json
from base64 import b64encode
from base64 import b64decode
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes


#get input from file as a string
with open('input.txt', 'r') as myfile:
    input = myfile.read().replace('\n', ' ')

#print (input)
#print()

key1 = ECC.generate(curve='P-256')

#print(key1.export_key(format='PEM'))
#print(key1)
print()

publickey = key1.public_key().export_key(format='PEM')

#pub = str(key1.public_key())
#publickey = (pub.split(', '))
#print(publickey[1], publickey[2])
# print(publickey)
# print()
# print (key1.d)
# print()

#encrypt using AES
data = bytes(input, 'utf-8')
key = bytes(str(key1.d), 'utf-8')
key = key[:16]
cipher = AES.new(key, AES.MODE_CFB)
ct_bytes = cipher.encrypt(data)
iv = b64encode(cipher.iv).decode('utf-8')
ct = b64encode(ct_bytes).decode('utf-8')
result = json.dumps({'iv':iv, 'ciphertext':ct})

print(result)

#decrypt using AES
json_input = input
b64 = json.loads(json_input)
nonce = b64decode(b64['nonce'])
ct = b64decode(b64['ciphertext'])
cipher = AES.new(key, AES.MODE_CFB, iv=iv)
pt = cipher.decrypt(ct)