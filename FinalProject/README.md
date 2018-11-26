# PRNG - Pseudo Random Number Generators

###### A PRNG is an algorithm that uses mathematical formulas to produce sequences of random numbers. A PRNG can start from a seed state (arbitrary start state) and can generate many numbers in a short time. A PRNG can even reproduce those numbers later if the starting(seed) state is known.

###### PRNG’s have 3 main characteristics: they are efficient, deterministic, and periodic.

1. Efficient: needs to be able to produce a large amount of numbers in a short time
2. Deterministic: should be able to reproduce the same numbers with the given starting point/seed
3. Periodic: the sequence of numbers will eventually repeat itself, but nowadays the periods are so long that this is rarely a cause of concern

###### Use in Cryptography:
- We can use PRNG’s to generate keys and encrypt data in cryptography. Many ciphers (like the block cipher) utilize random number generators to encrypt data. Some commonly used cryptographic PRNG’s are the xorshift, Mersenne-Twister, and u-rand(based off the Park-Miller PRNG). 

## Pseudo-Random Number Generators in this project:
###### Xorshift
- Xorshift random number generator is a type of pseudorandom number generator that is a subset of linear-feedback shift registers (LFSRs)  
- Generates the next number in the sequence by taking the exclusive or of a number with a bit-shifted version of itself
- Have to choose parameters carefully for a long period
- Xorshift generators are among the fastest and most efficient secure random number generators

###### Mersenne Twister
- Most widely used general purpose generator
- Its name comes from the fact that its period length is chosen to be a Mersenne prime

###### Park Miller
- Also called the Lehmer random number generator
- It is a type of linear congruential generator (LCG) that operates in multiplicative groups of integers modulo n
