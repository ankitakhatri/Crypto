'''
Simple RSA key implementation from scratch, using prime numbers
'''

import random

'''
First step is to implement Euclid's algorithm to determine the greatest common divisor between two numbers
https://www.geeksforgeeks.org/euclidean-algorithms-basic-and-extended/
'''

def euclid_gcd (x, y):
    if (x == 0):
        return y

    return (euclid_gcd(y%x, x))

'''
Then implement the extension of Euclid's algorithm with the extension to find the modular multiplicative inverse of two numbers
https://stackoverflow.com/questions/4798654/modular-multiplicative-inverse-function-in-python
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
https://www.daniweb.com/programming/software-development/code/216880/check-if-a-number-is-a-prime-number-python
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
https://www.geeksforgeeks.org/rsa-algorithm-cryptography/ (code is in C but concept is similar)
'''

def generate_keys(p, q):
    #input validation: check if p and q are prime and not equal to each other and move forward from there
    if not (is_prime(p) and is_prime(q)):
        print('Both numbers must be prime.')
        exit(1)
    elif p == q:
        print ('The two input numbers cannot be equal')
        exit(1)

    #n is the modulus
    n = p * q

    #calculate phi (totient of p and q)
    phi = (p - 1) * (q - 1)

    #public key is random num between 1 and phi, then run euclid_gcd on public key and phi to get final key
    public = random.randrange(1, phi)

    g = euclid_gcd(public, phi)
    while g != 1:
        public = random.randrange(1, phi)
        g = euclid_gcd(public, phi)

    #private key is modular inverse of public key and modulus
    private = mod_inv(public, n)

    #return public and private keypair (public key, modulus, private key, modulus)
    return ((public, n), (private, n))

'''
Encrypt the private key using the public key
Combined some different encryption methods to get this
'''
def encrypt(public, private):

    #use n and the public and private keys to come up with a longer encrypted key
    pubkey, n = public
    privkey, n = private
    cipher1 = pow(privkey, pubkey, n)
    cipher2 = pow(pubkey, privkey, n)
    encrypted = int(str(cipher1) + str(cipher2))
    return encrypted

'''
Take two primes as input and calculate public, private key pair, and encrypted key
'''

prime1 = int(input("Please enter a prime number (eg 3, 7, 19, 23)"))
prime2 = int(input("Please enter a second prime number"))

publicpair, privatepair = generate_keys(prime1, prime2)
public, n = publicpair
private, n = privatepair
print ("Public and private key pair: ", public, "," , private)
print ("Modulus: " , n)
print ("Encrypted key: ", encrypt(publicpair, privatepair))