"""File that executes test between the class methods of the Vector class and the equivalent numpy implementation on two arrays"""

import numpy as np
from functools import wraps
import time

from testFunctions import timing

def VectorTimer():
    for func in numpyMethodAnalogues.keys():
        print(f"Vector class implementation of f{numpyMethodAnalogues[func].__name__}")
        @timing
        def customTest():
            for _ in range(int(10**6)):
                a = Vector(2, 2).func()
                del a

        @timing
        def numpyTest():
            for _ in range(int(10**6)):
                a = np.array([2, 2]).numpyMethodAnalogues[func]()
                del a

        customTest()
        numpyTest()


if __name__ == "__main__":
    VectorTimer()
