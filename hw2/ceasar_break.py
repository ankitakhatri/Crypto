message = 'khoor zruog'
alphabet = 'abcdefghijklmnopqrstuvwxyz'

def ceasar_break():

	for key in range(len(alphabet)):
		cracked = ''
		for letter in message:
			if letter in alphabet:
				num = alphabet.find(letter)
				num = num - key

				if num < 0:
					num = num + len(alphabet)

				cracked = cracked + alphabet[num]

			else:
				cracked = cracked + letter


		print('Key #%s: %s' % (key, cracked))

ceasar_break()

