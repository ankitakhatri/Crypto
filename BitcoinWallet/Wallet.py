'''
Simple RSA key implementation from scratch, using prime numbers
'''

import random

'''
First step is to implement Euclid's algorithm to determine the greatest common divisor between two numbers
'''

def euclid_gcd (x, y):
    if (x == 0):
        return y

    return (euclid_gcd(y%x, x))

'''
Then implement the extension of Euclid's algorithm with the extension to find the modular multiplicative inverse of two numbers
'''

def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)

def mod_inv(a, b):
    g, x, y = egcd(a, b)
    if g != 1:
        raise Exception('The modular inverse of these numbers does not exist')
    else:
        return x % b

'''
Implement a function to test if a number is prime
'''

def is_prime(num):
    if num == 2:
        return True
    if num < 2 or num % 2 == 0:
        return False
    for n in range(3, int(num**0.5)+2, 2):
        if num % n == 0:
            return False
    return True

'''
Implement function to generate a public/private key pair using euclid_gcd, mod_inv, and is_prime
'''

def generate_keys(p, q):
    if not (is_prime(p) and is_prime(q)):
        print('Both numbers must be prime.')
        exit(1)
    elif p == q:
        print ('The two input numbers cannot be equal')
        exit(1)

    n = p * q

    phi = (p - 1) * (q - 1)

    public = random.randrange(1, phi)

    g = euclid_gcd(public, phi)
    while g != 1:
        public = random.randrange(1, phi)
        g = euclid_gcd(public, phi)

    # Use the extended version of Euclid's Algorithm to generate the private key

    private = mod_inv(public, phi)

    # Return public and private keypair

    return ((public, n), (private, n))

'''
Encrypt the private key using the public key
'''
def encrypt(public, private):

    #use n and the public and private keys to come up with a longer encrypted key
    pubkey, n = public
    privkey, n = private
    cipher1 = pow(privkey, pubkey, n)
    cipher2 = pow(pubkey, privkey, n)
    encrypted = int(str(cipher1) + str(cipher2))
    return encrypted

#testing each function
# c = euclid_gcd (9808234, 98328048)
# print (c)
#
# d = euclid_extended(35, 15)
# # print (d)
#
# print (is_prime(19))

public, private = generate_keys(37, 29)
print (public, private)
print (encrypt(public, private))




