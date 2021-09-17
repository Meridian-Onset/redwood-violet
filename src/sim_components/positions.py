# TODO: Allow checking for PositionUnboundedError when aligning move for actors

import numpy as np
from .configuration import config as cfg
from functools import wraps

FIELD_SIZE = cfg.conf['field_size']

class PositionUnboundedError(Exception):
    """Ignorable exception sub-class for specifying invalid initialization parameters"""
    def __init__(self, x, y, message = None):
        self.bad_x = x
        self.bad_y = y
        if message is None:
            message = self.construct_message()
        self.message = message

        super(PositionUnboundedError, self).__init__(self.message)

    def construct_message(self):
        if self.bad_x > FIELD_SIZE or self.bad_x < 0:
            x_message = f"x : {self.bad_x}\n"
        else : x_message = ""

        if self.bad_y > FIELD_SIZE or self.bad_y < 0:
            y_message = f"y : {self.bad_x}\n"
        else : y_message = ""

        return(f"Position outside simulation boundaries with {x_message}{y_message}")


class Vector_2D:
    """Generic position vector_2D class, designed to emulate a namedtuple, with
    baked-in Cartesian calculations and boundary checking"""
    def __init__(self, x, y, allow_out_of_bounds = False):
        try:
            if not (0 <= x < FIELD_SIZE) or not (0 <= y < FIELD_SIZE):
                raise PositionUnboundedError(x, y)

        except PositionUnboundedError:
            if allow_out_of_bounds: pass
            else:
                raise PositionUnboundedError(x, y)
        self.x = x
        self.y = y

     #TODO: make class iterable for unpacking in ensemble
    def __iter__(self):
        return iter([self.x, self.y])

    def __add__(self, other):
        return Vector_2D(
            self.x + other.x,
            self.y + other.y
        )

    def __sub__(self, other):
        return Vector_2D(
            self.x - other.x,
            self.y - other.y
        )

    def __mul__(self, other):
        #Note that this is the dot product of the vector_2Ds
        return self.x * other.x + self.y * other.y

    def __str__(self):
        return(f"x : {self.x}\ny : {self.y}")

    def distance_from(self, other):
        return np.sqrt((self.x-other.y)**2 + (self.y - other.y)**2)

    @property
    def magnitude(self):
        return self.distance_from(Vector_2D(0, 0))

    @property
    def unit(self):
        return Vector_2D(
            self.x / self.magnitude,
            self.y / self.magnitude
        )

    @property
    def theta_from_x(self):
        """Angle of vector_2D from the x axis"""
        return np.arcsin(self.y/self.magnitude)

    @property
    def theta_from_y(self):
        """Angle of vector_2D from the y axis"""
        return np.arcsin(self.x/self.magnitude)

#Dictionary of numpy analogues to the Vector_2D methods for testing purposes
# numpyMethodAnalogues = {
#     Vector_2D.__add__ : lambda x, randvals : np.add(x, np.array(randvals)),
#     Vector_2D.__sub__ : lambda x, randvals : np.subtract(x, np.array(randvals)),
#     Vector_2D.__mul__ : lambda x, randvals : np.dot(x, np.array(randvals)),
#     Vector_2D.magnitude : lambda x, randvals : np.linalg.norm(x),
#     Vector_2D.distance_from : lambda x, randvals : np.linalg.norm(x - np.array(randvals)),
#     Vector_2D.unit : lambda x, randvals : x / np.norm(x)
# }

if __name__ == "__main__":
    print("Compiled")
