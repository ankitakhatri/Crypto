# ECIES Homework Assignment
## Author: Ankita Khatri (CS 486, Cryptography, Professor Lambert)
### Due Date: November 7th
### Objective: Write a Python command line program that encrypts and decrypts files based on public key cryptography.

Python Version: 3.5 (PyCharm IDE)
Libraries Used: 
  1. pycryptodome (ECC and AES algorithms)
     - Pycryptodome has libraries to generate ECC keys based off a given curve
     - It also has built in AES algorithms for encryption and decryption (different modes-- I used Cipher Feedback Mode)
     - This library had all the functionality needed to create an ECC key and encrypt a file using that key and AES
  2. base64 (encode and decode)
  3. sys (command line functionality)

References/documentation for libraries:
1. https://pycryptodome.readthedocs.io/en/latest/src/public_key/ecc.html
2. https://pycryptodome.readthedocs.io/en/latest/src/cipher/aes.html?highlight=aes
3. https://pycryptodome.readthedocs.io/en/latest/src/cipher/classic.html#cfb-mode


Command line use:
```
python ./ecies.py e input.txt
python ./ecies.py d input.txt
```

Background Research:
- ECC (Elliptic Curve Cryptography) is a form of public key cryptography
 - The ECC key generator from the Pycryptodome library gives you points x and y on the curve, and d (private key)
 - You can use x and y as components of the public key for encryption and d as the private key for encryption
- For the purpose of this program, I converted d (private key technically) into bytes, parse the first 16 bytes, and fed that in as the key for the AES CFB encryption and decryption algorithm

The general steps:
1. Generate ECC key
2. Feed key into AES algorithm (Cipher Feedback Mode)
3. Use AES to encrypt/decrypt file

Sources:
- https://en.wikipedia.org/wiki/Integrated_Encryption_Scheme
- https://www.cryptopp.com/wiki/Elliptic_curve_integrated_encryption_scheme
- https://github.com/iCHAIT/Elliptical-Curve-Cryptography
