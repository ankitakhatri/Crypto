'''
PRNG based of XORshift algorithm.
https://en.wikipedia.org/wiki/Xorshift
'''
import time

class XORShiftRNG:
    def __init__(self):
        millis = int(round(time.time() * 1000))
        self.__init__(millis)

    def nextInt(self):
        self ^= (self << 13)
        print(self)
        self ^= (self >> 7)
        print(self)
        self ^= (self >> 5)
        print(self)

    nextInt(49302940)