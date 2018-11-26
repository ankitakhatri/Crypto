import time

class XORShiftRNG:
    def __init__(self):
        millis = int(round(time.time() * 1000))
        self.__init__(millis)


    def __init__(self, seed):
        self = seed

    def nextInt(self, max):
        self ^= (self << 1)
        print(self)
        self ^= (self << 1)
        print(self)
        self ^= (self << 1)
        print(self)

    nextInt(4098450349, 1)