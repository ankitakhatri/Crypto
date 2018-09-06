import re
from itertools import permutations

from math import log10

'''method to calculate fitness score using quadgrams and trigrams text files
    returns a score based on how similar the permutation is to plain english text
    reference/source code found from: http://practicalcryptography.com/cryptanalysis/text-characterisation/quadgrams/#a-python-implementation 
    http://practicalcryptography.com/media/cryptanalysis/files/ngram_score_1.py'''

class ngram_score(object):
    def __init__(self, ngramfile, sep=' '):
        ''' load a file containing ngrams and counts, calculate log probabilities '''
        self.ngrams = {}
        for line in file(ngramfile):
            key,count = line.split(sep) 
            self.ngrams[key] = int(count)
        self.L = len(key)
        self.N = sum(self.ngrams.itervalues())
        #calculate log probabilities
        for key in self.ngrams.keys():
            self.ngrams[key] = log10(float(self.ngrams[key])/self.N)
        self.floor = log10(0.01/self.N)

    def score(self,text):
        ''' compute the score of text '''
        score = 0
        ngrams = self.ngrams.__getitem__
        for i in xrange(len(text)-self.L+1):
            if text[i:i+self.L] in self.ngrams: score += ngrams(text[i:i+self.L])
            else: score += self.floor          
        return score

'''Using my own implementations of the Vigenere Cipher (encrypt and decrypt mehthods) from my first homework assignment. 
    The original implementation used the pycipher module'''

def vigEncrypt(input, key):

    keyLength = len(key)
    keyInt = [ord(i) for i in key]

    inputInt = [ord(i) for i in input]
    output = ''

    for char in range(len(inputInt)):
        if inputInt[char] == 32:
            output += " "
        else:
            ciphernum = (inputInt[char] + keyInt[char % keyLength]) % 26
            cipherchar = chr(ciphernum + 65).lower()
            output += cipherchar

    return (output)

def vigDecrypt(input, key):
    keyLength = len(key)
    keyInt = [ord(i) for i in key]
    inputInt = [ord(i) for i in input]
    output = ''
    for char in range(len(inputInt)):
        if inputInt[char] == 32:
            output += " "
        else:
            ciphernum = (inputInt[char] - keyInt[char % keyLength]) % 26
            cipherchar = chr(ciphernum + 65).lower()
            output += cipherchar
    return (output)

''' class to store the 'best' permutations, higher scores mean less fitness, lower scores preferred '''

#keep a list of the best scores 
class best(object):
    def __init__(self, N):
        self.store = []
        self.N = N
        
    def add(self,item):
        self.store.append(item)
        self.store.sort(reverse=True)
        self.store = self.store[:self.N]
    
    def __getitem__(self,k):
        return self.store[k]

    def __len__(self):
        return len(self.store)

#only going to use quadgram instead of both tri and quadgram scores
#the text says anything higher than quadgram isn't very accurate

qgram = ngram_score('quadgrams.txt')

#get encrypted text using encrypt method
ciphertext = vigEncrypt('hello world', 'pizza')

#print the cipher text
print (ciphertext)

#set size of the 'best' list to 50
size = 50

#checking for key lengths of 3, 4, 5, 6, 7, 8, 9, and 10
for keylen in range(3, 11):

    bestlist = best(size)

    for i in permutations ('ABCDEFGHIJKLMNOPQRSTUVWXYZ', 3):

        key = ''.join(i) + 'A'*(keylen-len(i))
        plaintext = vigDecrypt(key, ciphertext)
        score = 0

        for j in range(0,len(ciphertext), keylen):
            score += qgram.score(plaintext[j:j+3])
        bestlist.add((score,''.join(i),plaintext[:30]))

    next_rec = best(size)

    for i in range(0, keylen-3):
        for k in xrange(size):
            for c in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
                key = bestlist[k][1] + c
                fullkey = key + 'A'*(keylen-len(key))
                plaintext = vigDecrypt(fullkey, ciphertext)
                score = 0
                for j in range(0,len(ciphertext), keylen):
                    score += qgram.score(plaintext[j:j+len(key)])
                next_rec.add((score, key, plaintext[:30]))
        bestlist = next_rec
        next_rec = best(size)

    bestkey = bestlist[0][1]
    plaintext = vigDecrypt(bestkey, ciphertext)
    bestscore = qgram.score(plaintext)

    for i in range(size):
        plaintext = vigDecrypt(bestlist[i][1], ciphertext)
        score = qgram.score(plaintext)
        if score > bestscore:
            bestkey = bestlist[i][1]
            bestscore = score 

    print round(bestscore, 2), 'Vigenere Key Length of', keylen, ':"' + bestkey + '",' , vigDecrypt(bestkey, ciphertext)

