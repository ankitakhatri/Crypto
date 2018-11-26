import time

class XORShiftRNG:
    def __init__(self):
        millis = int(round(time.time() * 1000))
        self.__init__(millis)

    def nextInt(self):
        self ^= (self << 1)
        print(self)
        self ^= (self << 10)
        print(self)
        self ^= (self >> 20)
        print(self)

    nextInt(49302940)