# RSA Python Implementation README

## Objective: Research how RSA key generation works and come up with a simple implementation

###### Preliminary Research on RSA Keys + Design for Assignment
- RSA is an asymmetric key system that creates a public,private key pair
- It is typically used with large prime numbers
- This link has a simple explanation of the math behind RSA keys
  - https://hackernoon.com/how-does-rsa-work-f44918df914b
  
- I first needed to implement both the Euclidean and Extended Euclidean algorithm
  - The Euclidean algorithm finds the greatest common divisor between two numbers
  - The Extended Euclidean algorithm can be implemented to find the modular multiplicative inverse between two numbers
    - According to Wikipedia: "In mathematics, in particular the area of number theory, a modular multiplicative inverse of an integer a is an integer x such that the product ax is congruent to 1 with respect to the modulus m.[1] In the standard notation of modular arithmetic this congruence is written as"
    - References
      - https://en.wikipedia.org/wiki/Modular_multiplicative_inverse
      - https://stackoverflow.com/questions/4798654/modular-multiplicative-inverse-function-in-python
      - https://en.wikipedia.org/wiki/Extended_Euclidean_algorithm
      - https://www.geeksforgeeks.org/euclidean-algorithms-basic-and-extended/
      
- After implementing both versions of Euclidean's algorithm, I needed to implement a basic function that checks for prime numbers
- Next came the most important step: generating the key pairs 
  1. Pick two prime numbers, p and q, I take them as the input for my function
  2. Check that the numbers are prime and move forward from there
  3. Multiple p and q (I store this as n and use it as the modulus later for encryption)
  4. Calculate phi= (p-1) * (q-1), choose a number between 1 and phi, and implement Euclid's gcd algorithm to generate a public key
  5. To generate the private key, find the modular multiplicative inverse of the public key and n (the modulus)
  6. Encrypt using pow(x, y, mod) as pow(public, private, n)
      
     
