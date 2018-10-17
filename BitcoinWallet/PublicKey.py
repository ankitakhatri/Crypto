#idea of how to create a public key from the private key

#use built-in python function (is that part allowed? have to check with professor)
#suggested was to generate using private key * generator for curve 

#need to figure out a way to store this in a pair with the private key (hash map)

publicKey = private_key.to_public()
#convert to hex form (public_key is already in hex so may not be neccessary)
publicKey.hex()