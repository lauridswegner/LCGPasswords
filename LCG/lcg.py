import os
import time
from typing import Optional

class LCGPseudoRandomizer:

    def __init__(self, m: int = 2**63, a: int = 6364136223846793005, c: int = 1, seed: Optional[int] = None): # Newlib

        self.m: int = m
        self.a: int = a
        self.c: int = c

        if seed is None:
            # Read 8 random bytes from /dev/urandom
            random_bytes = os.urandom(8)
            # Convert the random bytes to an integer
            self.x0: int = int.from_bytes(random_bytes, byteorder='big')
        else:
            self.x0: int = seed
        self.x_prev: int = (self.a * self.x0 + self.c) % self.m

    def randomint(self, lower_limit: Optional[int] = None, upper_limit: Optional[int] = None) -> int:

        self.x_prev = (self.a * self.x_prev + self.c) % self.m

        if (lower_limit != None and upper_limit != None):
            return int((self.x_prev / (self.m -1)) * (upper_limit - lower_limit) + lower_limit)
        else:
            return self.x_prev
        

lcg = LCGPseudoRandomizer()
print(lcg.randomint(1,101))
print(lcg.randomint(1,101))
print(lcg.randomint(1,101))
print(lcg.randomint(1,101))
print(lcg.randomint(1,101))