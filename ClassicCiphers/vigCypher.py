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

    return (output)

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
    return (output)

print (vigEncrypt("ATTACK AT DAWN", "PIZZA"))
print (vigDecrypt("PBSZCZ ZS SIVM", "PIZZA"))