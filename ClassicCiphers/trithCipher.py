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

    return (output)

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
    return (output)

print (trithEncrypt("ATTACK AT DAWN"))
print (trithDecrypt("AUVDGP HB NLIA"))