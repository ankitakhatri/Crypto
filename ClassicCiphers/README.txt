Read Me:

Name: Ankita Khatri
Class: Cryptography
Assignment: Homework #1- Classical Ciphers
Python Version: 3.5.2

Description:
    -I have written 5 different ciphers and have them as their own methods
    -Combined all of them with file input + file output, and command line arguments, in ClassicCiphers.py
    -Am not comfortable with python OOP, which is why I am submitting so many different files
    -Provided comments in my code but more detailed explanation for running through command line below

 1. Caesar Cipher
    -input: text to be decrypted or encrypted
    -command line: python ClassicCiphers.py file.txt -caesar e/d

 2. Transposition Cipher
    -input: text to be decrypted/encrypted, int key (columnar transposition)
    -command line: python ClassicCiphers.py file.txt -transpo key e/d

 3. Trithemius Cipher
    -specific implementation of Vigenere cipher so key is set
    -other input: text to be decrypted/encrypted
    -command line: python ClassicCiphers.py file.txt -trith e/d

 4. Vigenere Cipher
    -input: string key and input text to encrypt/decrypt
    -command line: python ClassicCiphers.py file.txt key -vig e/d

 5. Substitution Cipher
    -input: text to decrypt/encrypt (alphabetical only)
    -command line: python ClassicCiphers.py file.txt -sub e/d

 More References: http://practicalcryptography.com/ciphers/classical-era/
 https://en.wikipedia.org/wiki/Classical_cipher
 https://www.tutorialspoint.com/cryptography_with_python/cryptography_with_python_transposition_cipher.html
 https://github.com/CryptoUSF/Course-Material/blob/master/references/books/1910%20-%20Manual%20for%20the%20Solution%20of%20Military%20CIphers.pdf
 https://github.com/CryptoUSF/Course-Material/blob/master/references/books/1945%20-%20The%20Mathamatical%20Theory%20of%20Cryptography.pdf



