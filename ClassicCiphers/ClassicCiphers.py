import math
import sys


# Adding all the five ciphers w/ command line capabilities
# Not familiar with python object oriented-- doing it all in one method

# Caesar Cipher

# Simple Caesar cipher implementation.
# Encrypt and Decrypt functions with set shift of 3, which is the classic shift.
# References: https://en.wikipedia.org/wiki/Caesar_cipher

def caesarencrypt(input):
    # shift
    index = 3
    output = ""
    for char in input:
        # keep spaces as is
        if char == " ":
            output += " "
        else:
            # shift all other characters down 3
            ciphernum = ord(char) + index
            cipherchar = chr(ciphernum)
            output += cipherchar

    print("Input Text:", input)
    print("Encrypted Text:", output)


def caesardecrypt(input):
    # shift
    index = 3
    output = ""
    for char in input:
        # keep spaces as is
        if char == " ":
            output += " "
        else:
            # shift all other characters up 3
            ciphernum = ord(char) - index
            cipherchar = chr(ciphernum)
            output += cipherchar

    print("Encrypted Text:", input)
    print("Decrypted Text:", output)


# Transposition Cipher
# Columnar Transposition
# References: http://crypto.interactive-maths.com/simple-transposition-ciphers.html
def transpoEncrypt(key, input):
    # creating a table to collect output based on key
    outputTable = [''] * key

    # iterating through columns to fill out the table
    for col in range(key):
        pos = col
        while pos < len(input):
            outputTable[col] += input[pos]
            pos += key

    # print the table to show encrypted input
    return(''.join(outputTable))


def transpoDecrypt(key, input):
    # find number of columns in original table
    columns = math.ceil(len(input) / key)
    rows = key
    # box refers to the number of 'boxes' filled in the table
    box = (columns * rows) - len(input)
    # output table to store original text
    outputTable = [''] * columns
    # pointers to iterate through columns and rows
    col = 0
    row = 0

    # iterate through letters in the input (encrypted text)
    for char in input:
        # add to output (decrypted text)
        outputTable[col] += char
        # iterate through columns (columnar transposition)
        col += 1
        # increment row when you go through the column
        if (col == columns) or (col == columns - 1 and row >= rows - box):
            col = 0
            row += 1

    return(''.join(outputTable))


# Simple substitution cipher
# Uses a predefined key (in this case, the alphabet backwards)
# Substitutes each letter in the input with letter from the key
# References: https://en.wikipedia.org/wiki/Substitution_cipher
# Limitations: changes uppercase letters to lowercase to find in key (which is only lowercase alphabet)
# Only alphabet not alphanumeric key (can be changed easily, just how I set it up)

def subEncrypt(input):
    output = ""
    letters = "abcdefghijklmnopqrstuvwxyz"
    # set key-- alphabet backwards
    key = "zyxwvutsrqponmlkjihgfedcba"

    for char in input:
        # keep spaces as is
        if char == " ":
            output += " "
        else:
            # substitute based on index of alphabet and key
            ciphernum = letters.index(char.lower())
            cipherchar = key[ciphernum]
            output += cipherchar

    return (output)


def subDecrypt(input):
    output = ""
    letters = "abcdefghijklmnopqrstuvwxyz"
    # key is alphabet backwards
    key = "zyxwvutsrqponmlkjihgfedcba"

    for char in input:
        # keep spaces as is
        if char == " ":
            output += " "
        else:
            # subsitute backwards to get original text
            ciphernum = key.index(char.lower())
            cipherchar = letters[ciphernum]
            output += cipherchar

    return(output)


# Trithemius
# Specific implementation of Vigenere Cipher with a specific key
# key = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
# References: http://www.crypto-it.net/eng/simple/trithemius-cipher.html?tab=0
# Limitations: changes all characters to lower case, can be changed easily

def trithEncrypt(input):
    key = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'.lower()
    keyLength = len(key)
    keyInt = [ord(i) for i in key]

    inputInt = [ord(i) for i in input]
    output = ''

    for char in range(len(inputInt)):
        if inputInt[char] == 32:
            output += " "
        else:
            ciphernum = (inputInt[char] + keyInt[char % keyLength]) % 26
            cipherchar = chr(ciphernum + 65)
            output += cipherchar.lower()

    return(output)


def trithDecrypt(input):
    key = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    keyLength = len(key)
    keyInt = [ord(i) for i in key]
    inputInt = [ord(i) for i in input]
    output = ''
    for char in range(len(inputInt)):
        if inputInt[char] == 32:
            output += " "
        else:
            ciphernum = (inputInt[char] - keyInt[char % keyLength]) % 26
            cipherchar = chr(ciphernum + 65)
            output += cipherchar.lower()
    return(output)


# Polyalphabetic cipher- Vigenere Cipher
# Uses multiple Caesar ciphers to shift each letter in input based on the key
# References: https://en.wikipedia.org/wiki/Vigen%C3%A8re_cipher
# Limitations: converts all characters to lowercase, can be changed, just how I set it up

def vigEncrypt(input, key):
    keyLength = len(key)
    keyInt = [ord(i) for i in key]

    inputInt = [ord(i) for i in input]
    output = ''

    for char in range(len(inputInt)):
        if inputInt[char] == 32:
            output += " "
        else:
            ciphernum = (inputInt[char] + keyInt[char % keyLength]) % 26
            cipherchar = chr(ciphernum + 65).lower()
            output += cipherchar

    return(output)


def vigDecrypt(input, key):
    keyLength = len(key)
    keyInt = [ord(i) for i in key]
    inputInt = [ord(i) for i in input]
    output = ''
    for char in range(len(inputInt)):
        if inputInt[char] == 32:
            output += " "
        else:
            ciphernum = (inputInt[char] - keyInt[char % keyLength]) % 26
            cipherchar = chr(ciphernum + 65).lower()
            output += cipherchar
    return(output)


# for command line args

# command line args: file, flag, key, e or d (encrypt or decrypt)
# flag options: -ceasar, -transpo, -sub, -trith, -vig

def cipher():
    if len(sys.argv) == 5:
        file = sys.argv[1]
        flag = sys.argv[2]
        key = sys.argv[3]
        mode = sys.argv[4]
    else:
        if len(sys.argv) == 4:
            file = sys.argv[1]
            flag = sys.argv[2]
            mode = sys.argv[3]

    # print (file, flag, key, mode)

    # get input from file

    with open(file, 'r') as myfile:
        input = myfile.read().replace('\n', ' ')

    # open file to write output
    f = open("encrypted.txt", "w")

    f.write("Input: ")
    f.write (input)
    f.write (" ")

    f.write("Output: ")

    # print (file, flag, mode)

    if flag == '-caesar':
        if mode == 'e':
            f.write(caesarencrypt(input))
        else:
            if mode == 'd':
                f.write(caesardecrypt(input))

    if flag == '-transpo':
        if mode == 'e':
            intkey = int(key)
            f.write(transpoEncrypt(intkey, input))
        else:
            if mode == 'd':
                intkey = int(key)
                f.write(transpoDecrypt(intkey, input))

    if flag == '-sub':
        if mode == 'e':
            f.write(subEncrypt(input))
        else:
            if mode == 'd':
                f.write(subDecrypt(input))

    if flag == '-trith':
        if mode == 'e':
            f.write(trithEncrypt(input))
        else:
            if mode == 'd':
                f.write(trithDecrypt(input))

    if flag == '-vig':
        if mode == 'e':
            f.write(vigEncrypt(input, key))

        else:
            if mode == 'd':
                f.write(vigEncrypt(input, key))

cipher()
