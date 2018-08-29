# Simple substitution cipher
# Uses a predefined key (in this case, the alphabet backwards)
# Substitutes each letter in the input with letter from the key
# References: https://en.wikipedia.org/wiki/Substitution_cipher
# Limitations: changes uppercase letters to lowercase to find in key (which is only lowercase alphabet)
# Only alphabet not alphanumeric key (can be changed easily, just how I set it up)

def subEncrypt(input):

    output = ""
    letters = "abcdefghijklmnopqrstuvwxyz"
    #set key-- alphabet backwards
    key = "zyxwvutsrqponmlkjihgfedcba"

    for char in input:
        #keep spaces as is
        if char == " ":
            output += " "
        else:
            #substitute based on index of alphabet and key
            ciphernum = letters.index(char.lower())
            cipherchar = key[ciphernum]
            output += cipherchar

    return ("Input Text:", input, "Encrypted Text:", output)


def subDecrypt(input):

    output = ""
    letters = "abcdefghijklmnopqrstuvwxyz"
    #key is alphabet backwards
    key = "zyxwvutsrqponmlkjihgfedcba"

    for char in input:
        #keep spaces as is
        if char == " ":
            output += " "
        else:
            #subsitute backwards to get original text
            ciphernum = key.index(char.lower())
            cipherchar = letters[ciphernum]
            output += cipherchar

    return ("Encrypted Text:", input, "Decrypted Text:", output)


input1 = "hello world"
print (subEncrypt(input1))

print ()

input2 = "svool dliow"
print (subDecrypt(input2))