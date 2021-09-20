import numpy as np
from typing import Dict

from configuration import config as cfg

FIELD_SIZE = cfg.conf['field_size']


class PositionUnboundedError(Exception):
    """Ignorable exception sub-class for specifying invalid initialization parameters TODO: Only pass in bad params"""
    def __init__(self, bad_positions : Dict[str, float], message = None):
        
        self.bad_positions = bad_positions
        if message is None:
            self.message = self.construct_message()

        super(PositionUnboundedError, self).__init__(self.message)

    def construct_message(self):
        iter_message = ""
        for key in self.bad_positions.keys():
            iter_message = iter_message + f"\n{key} : {self.bad_positions[key]}"

        return(f"Position outside simulation boundaries with {iter_message}")


class Vector_2D:
    """Generic position vector_2D class, designed to emulate a namedtuple, with
    baked-in Cartesian calculations and boundary checking"""

    def __init__(self, x, y, allow_out_of_bounds = False):

        bad_params = dict()
        if not (0 <= x < FIELD_SIZE): bad_params['x']= x
        if not (0 <= y < FIELD_SIZE): bad_params['y']= y
        if len(bad_params) != 0 and not allow_out_of_bounds:
            raise PositionUnboundedError(bad_params)
            
        self.x = x
        self.y = y
        self._getter_dict = {
            "x" : self.x,
            "y" : self.y
            }

    def keys(self):
        return ["x", "y"]

    def __getitem__(self, key):
        return self._getter_dict[key]

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
    positions = {'x' : 1}
    positions2 = {'x' : 2, 'y' : 3}
    positions3 = {'y' : 4}
    

