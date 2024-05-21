import os
import time
from typing import Optional

class LCGPseudoRandomizer:

    def __init__(self, m: int = 2**63, a: int = 6364136223846793005, c: int = 1, seed: Optional[int] = None): # Newlib

        self.m: int = m
        self.a: int = a
        self.c: int = c

        if seed is None:

            self.x0: int = int(os.getpid() + time.time()) * time.monotonic_ns()

        else:

            self.x0: int = seed

        self.x_prev: int = (self.a * self.x0 + self.c) % self.m

    def randomint(self, lower_limit: Optional[int] = None, upper_limit: Optional[int] = None) -> int:

        self.x_prev = (self.a * self.x_prev + self.c) % self.m

        if (lower_limit != None and upper_limit != None):

            return int((self.x_prev / (self.m -1)) * (upper_limit - lower_limit) + lower_limit)
        
        else:

            return self.x_prev
        
    def randomchoice(self, input_str: str):

        string_length = len(input_str)

        if string_length > 1:
            
            lower_limit: int = 0
            upper_limit: int = string_length

            return input_str[self.randomint(lower_limit, upper_limit)]

        else:
            return input_str