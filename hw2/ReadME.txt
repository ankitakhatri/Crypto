README

Author: Ankita Khatri
Class: Cryptography
Python Version: python 2.7 (Mac Default)

Description: This homework contains a method to break the ceasar cipher with brute force, a working version of the n-gram provided by the professor, and a class that analyzes possible keys for the vigenere cipher.

Ceasar Cipher
  Reference: https://inventwithpython.com/hacking/chapter7.html

N-gram:
  Takes input text file and asks for numbers for n in the n-gram analysis
  
Breaking vigenere cipher:
  Performs a quadgram score using given ngram_score code. Implements my original vigenere cip.her.
  Tests possible alphabet permutations from length 3-10, scores them using quadgram.txt file
  Collects the lowest scores (better fitness, more common in english language) and tries to guess closest key of each length.
  Prints best key in each length category.
 
Run all python files in terminal.:

Example: python ceasar_break.py
python break_vigenere.py

Sources: http://practicalcryptography.com/media/cryptanalysis/files/ngram_score_1.py
http://practicalcryptography.com/cryptanalysis/text-characterisation/quadgrams/#a-python-implementation
http://practicalcryptography.com/media/cryptanalysis/files/break_vigenere.py
http://practicalcryptography.com/cryptanalysis/stochastic-searching/cryptanalysis-vigenere-cipher-part-2/
http://practicalcryptography.com/cryptanalysis/stochastic-searching/cryptanalysis-vigenere-cipher/
https://github.com/CryptoUSF/Course-Material/blob/master/code/cipher.py#L276-L306 (code given by professor)
