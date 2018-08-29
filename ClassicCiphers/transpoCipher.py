# Transposition Cipher
# Columnar Transposition
# References: http://crypto.interactive-maths.com/simple-transposition-ciphers.html

import math
def transpoEncrypt(key, input):

    #creating a table to collect output based on key
    outputTable = [''] * key

    #iterating through columns to fill out the table
    for col in range(key):
        pos = col
        while pos < len(input):
            outputTable [col] += input[pos]
            pos += key

    #print the table to show encrypted input
    return (''.join(outputTable))

def transpoDecrypt(key, input):
    #find number of columns in original table
    #using math.ceil to round up the decimal number
    columns = math.ceil(len(input) / key)
    rows = key
    #box refers to the number of 'boxes' filled in the table
    box = (columns * rows) - len(input)
    #output table to store original text
    outputTable = [''] * columns
    #pointers to iterate through columns and rows
    col = 0
    row = 0

    #iterate through letters in the input (encrypted text)
    for char in input:
        #add to output (decrypted text)
        outputTable[col] += char
        #iterate through columns (columnar transposition)
        col += 1
        #increment row when you go through the column
        if (col == columns) or (col == columns - 1 and row >= rows - box):
            col = 0
            row += 1

    return (''.join(outputTable))


print (transpoEncrypt(8, 'Common sense is not so common.'))
print()
print (transpoDecrypt(8,'Cenoonommstmme oo snnio. s s c' ))