# Simple Caesar cipher implementation.
# Encrypt and Decrypt functions with set shift of 3, which is the classic shift.
# References: https://en.wikipedia.org/wiki/Caesar_cipher

def caesarencrypt (input):
    #shift
    index = 3
    output = ""
    for char in input :
        #keep spaces as is
        if char == " ":
            output += " "
        else:
            #shift all other characters down 3
            ciphernum = ord(char) + index
            cipherchar = chr(ciphernum)
            output += cipherchar

    return ("Input Text:", input, "Encrypted Text:", output)

def caesardecrypt (input):
    #shift
    index = 3
    output = ""
    for char in input :
        #keep spaces as is
        if char == " ":
            output += " "
        else:
            #shift all other characters up 3
            ciphernum = ord(char) - index
            cipherchar = chr(ciphernum)
            output += cipherchar

    return ("Encrypted Text:", input, "Decrypted Text:", output)

input1 = "hello world"
input2 = "khoor zruog"
index = 3
print (caesarencrypt (input1))
print ()
print (caesardecrypt (input2))