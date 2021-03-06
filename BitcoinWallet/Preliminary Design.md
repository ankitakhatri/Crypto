﻿
 Preliminary Design for Bitcoin Wallet based on class discussion
 
   What I have so far:
 - Research done on how I want to set up the wallet
 - Some starter code to implement this design
 - Ideas on how to generate and store keys, found code for base58 encoding, list of other functions I may implement
 
 *Edit from Wednesday morning's class-- we are all going to be generating RSA public/private key pairs*
 1. Make public/private keys
   1. Research
      1. Generating public and private keys, public keys are derived from private keys
      2. Public keys are generated to show ownership of a Bitcoin
      3. Public key is an (x ,y) coordinate on an Elliptic Curve
   2. Professor’s suggestion: 
      1. Private keys are just a U Random within a certain size (mod the order of the curve) 
      -  This isn't very secure, RNG's in python use the same seeds
      -  To make it more cryptographically secure, use the python RNG that's specifically for cryptography (import secrets module, available in python 3.6 and newer) 
      2. Public key is just equal to the private key * generator for the curve
      3. Have a class for public and private key
2. Wallet class
   1. Operations that will make it useful
      1. Def list
         1. Return a list of key pairs/entire wallet
         2. Text representation
      2. Def newKeyPair
         1. Create a new public/private key pair
         2. Store it securely
      3. Def display
         1. Display a certain public key
         2. Planning to display as a QR code (in the terminal)
      4. Base58Check
         1. Used to encode bitcoin addresses
         2. Binary to text encoding scheme, represents large integers as alphanumeric text
         3. Pay-to-pubkey-hash (p2pkh): payload is RIPEMD160(SHA256(ECDSA_publicKey)) where ECDSA_publicKey is a public key the wallet knows the private key for; version 0x00 (these addresses begin with the digit '1')
         4. Create a wallet directory, ssh file, persistence to store and move keys
         
  Sources: 
- https://medium.freecodecamp.org/how-to-generate-your-very-own-bitcoin-private-key-7ad0f4936e6c
- https://medium.com/coinmonks/private-and-public-key-cryptography-explained-simply-4c374d371736
- https://bitcoin.stackexchange.com/questions/75677/python-bitcoinlib-create-private-keys-public-keys-and-addresses-how-to-do-i
- https://en.bitcoin.it/wiki/Base58Check_encoding
- https://en.wikipedia.org/wiki/Base58
- https://en.bitcoinwiki.org/wiki/Base58
- https://github.com/bitcoin/bitcoin/blob/master/src/base58.h
