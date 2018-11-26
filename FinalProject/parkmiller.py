import math
import time


class ParkMiller:

    def __init__(self, low=0, high=0):
        if (low < 2):
            low = 2
        if (high < 2):
            high = 9223372036854775807
        self.m_min = low
        self.m_max = high
        self.m_seed = time.time()

    def Seed(self, seed):
        self.m_seed = seed

    def Next(self):
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

        if (self.m_seed < a):
            self.m_seed += a

        return int(self.m_seed)


def test():

    random = ParkMiller(10, 13901309)
    random.Seed(2308094)
    for x in range(10):
        print("%d  " % random.Next())


if __name__ == '__main__':
    test()