'''Break the ceasar cipher by brute force by testing every single possible key '''

#usingthe encrypted text from my version of the caesar cipher from hw1
ciphertext = 'khoor zruog'
alphabet = 'abcdefghijklmnopqrstuvwxyz'

def ceasar_break():

	for key in range(len(alphabet)):
		cracked = ''
		#check each letter in the ciphertext, shift by key(all 25 keys)
		for letter in ciphertext:
			if letter in alphabet:
				num = alphabet.find(letter)
				num = num - key
				
				if num < 0:
					num = num + len(alphabet)

				cracked = cracked + alphabet[num]

			else:
				cracked = cracked + letter

		#print all 25 cracked possibilited, one will be the correct plaintext
		print('Key #%s: %s' % (key, cracked))

ceasar_break()

