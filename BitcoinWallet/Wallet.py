'''
Simple RSA key implementation from scratch, using prime numbers
'''

import random

'''
First step is to implement Euclid's algorithm to determine the greatest common divisor between two numbers
'''

def euclid (x, y):
    while y != x:
        x, y = y, x % y
    return x



