"""Generic position vector class, designed to emulate a namedtuple, with
baked-in Cartesian calculations and boundary checking"""

# TODO: Allow checking for PositionUnboundedError when aligning move for actors

import numpy as np
from config import field_size
from functools import wraps
from promise import Promise

class PositionUnboundedError(Exception):
    def __init__(self, x, y, message = None):
        self.bad_x = x
        self.bad_y = y
        if message is None:
            message = self.construct_message()
        self.message = message

        super(PositionUnboundedError, self).__init__(self.message)

    def construct_message(self):
        if self.bad_x > field_size | self.bad_x < 0:
            x_message = f"x : {self.bad_x}\n"
        else : x_message = ""

        if self.bad_y > field_size | self.bad_y < 0:
            y_message = f"y : {self.bad_x}\n"
        else : y_message = ""

        return(f"Position outside simulation boundaries with {x_message}{y_message}")

"""def bounding_promise(func):
    #Boundary Checking Promise
    @wraps(func)
    def position_promise_wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print(result.x, result.y)
        if result.x < 0 | result.x > field_size:
            raise PositionUnboundedError(result)
        elif result.y < 0 | result.y > field_size:
            raise PositionUnboundedError(result)
        else:
            return result

    return position_promise_wrapper"""


class Vector:
    def __init__(self, x, y):
        print(0 < x < field_size)
        if not (0 < x < field_size):
            raise PositionUnboundedError(x, y)
        if not (0 < y < field_size):
            raise PositionUnboundedError(x, y)
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(
            self.x + other.x,
            self.y + other.y
        )

    def __sub__(self, other):
        return Vector(
            self.x - other.x,
            self.y - other.y
        )

    def __mul__(self, other):
        #Note that this is the dot product of the vectors
        return self.x * other.x + self.y * other.y

    def __str__(self):
        return(f"x : {self.x}\ny : {self.y}")

    def distance_from(self, other):
        """Takes another Position object as argument and calculates the distance between the two"""
        return np.sqrt((self.x-other.y)**2 + (self.y - other.y)**2)

    @property
    def magnitude(self):
        return self.distance_from(self, Vector(0, 0))

    @property
    def unit(self):
        return Vector(
            self.x / self.magnitude,
            self.y / self.magnitude
        )

    def cross_product(self, other): #TODO
        pass

if __name__ == "__main__":
    test = Vector(-1, -4)
    test2 = Vector(3,4)

    test - test2
