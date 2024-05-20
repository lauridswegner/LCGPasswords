import os
import time
from typing import Optional

class LCGPseudoRandomizer:

    def __init__(self, m=2**63, a=6364136223846793005, c=1, seed=None): # Newlib

        self.m = m
        self.a = a
        self.c = c

        if seed is None:
            self.x0 = int(os.getpid() + time.time()) * time.monotonic_ns()
        else:
            self.x0 = seed

        self.x_prev = (self.a * self.x0 + self.c) % self.m

    def randomint(self, lower_limit=None, upper_limit=None):

        self.x_prev = (self.a * self.x_prev + self.c) % self.m

        if (lower_limit != None and upper_limit != None):
            return int((self.x_prev / (self.m -1)) * (upper_limit - lower_limit) + lower_limit)
        else:
            return self.x_prev
        

lcg = LCGPseudoRandomizer()
print(lcg.randomint(1,101))