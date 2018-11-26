import math
import time


class MyRNG:

    def __init__(self, low=0, high=0):
        #     The constructor initializes data members "m_min" and "m_max"
        if (low < 2):
            low = 2
        if (high < 2):
            high = 9223372036854775807
        self.m_min = low
        self.m_max = high
        self.m_seed = time.time()

    def Seed(self, seed):
        #  Seed the generator with 'seed'
        self.m_seed = seed

    def Next(self):
        #     Return the next random number using an algorithm based on the
        #        Park & Miller paper "RANDOM NUMBER GENERATORS: GOOD ONES ARE
        #        HARD TO FIND"
        a = self.m_min
        m = self.m_max
        q = math.trunc(m / a)
        r = m % a

        hi = self.m_seed / q
        lo = self.m_seed % q
        x = (a * lo) - (r * hi)

        if (x < a):
            x += a

        self.m_seed = x
        self.m_seed %= m

        # ensure that the random number is not less
        # than the minimum number within the user specified range
        if (self.m_seed < a):
            self.m_seed += a

        return int(self.m_seed)


def test():
    #  Simple test function to see if the functionality of my class
    #     is there and works

    random = MyRNG(7, 1987)
    random.Seed(806189064)
    for x in range(15):
        print("%d,  " % (random.Next()), end="")


if __name__ == '__main__':
    test()