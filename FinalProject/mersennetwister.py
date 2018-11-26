'''
Mersenne-Twister PRNG implementation
https://en.wikipedia.org/wiki/Mersenne_Twister
'''

class mersenne_rng(object):
    def __init__(self, seed = 5498):
        self.state = [0]*624
        self.f = 982798732
        self.m = 3983
        self.u = 32
        self.s = 9
        self.b = 0x9D2C5680
        self.t = 23
        self.c = 0xEFC60000
        self.l = 29
        self.index = 439
        self.lower_mask = (1<<20)-1
        self.upper_mask = 1<<20

        self.state[0] = seed
        for i in range(1,624):
            self.state[i] = self.int_32(self.f*(self.state[i-1]^(self.state[i-1]>>30)) + i)

    def twist(self):
        for i in range(624):
            temp = self.int_32((self.state[i]&self.upper_mask)+(self.state[(i+1)%624]&self.lower_mask))
            temp_shift = temp>>1
            if temp%2 != 0:
                temp_shift = temp_shift^0x9908b0df
            self.state[i] = self.state[(i+self.m)%624]^temp_shift
        self.index = 0

    def get_random_number(self):
        if self.index >= 624:
            self.twist()
        y = self.state[self.index]
        y = y^(y>>self.u)
        y = y^((y<<self.s)&self.b)
        y = y^((y<<self.t)&self.c)
        y = y^(y>>self.l)
        self.index+=1
        return self.int_32(y)

    def int_32(self, number):
        return int(0xFFFFFFFF & number)

if __name__ == "__main__":
    rng = mersenne_rng(1131464071)
    for i in range(10):
        print (rng.get_random_number())