import numpy as np
from typing import Dict

from sim_components.configuration import config as cfg
from sim_components.positions import Vector_2D

NUTRITIVE_VALUE = cfg.conf['food_values']['default_nutritive_value']


class Instance:
    '''Standard reward type, no change to actor stats, food and poison inherit from this class'''

    def __init__(self, field_size, rotten_chance=0):
        x = np.random.random() * field_size
        y = np.random.random() * field_size

        self.position = Vector_2D(x, y)
        self.rotten_chance = rotten_chance
        self.rotten = (np.random.random() < rotten_chance)
        self.eaten = False

    def consume(self) -> Dict[str, float]:
        """The consume method pops the attribute additives to the consumer."""
        self.eaten = True  # value to apply a mask to in ensemble object
        return({
                'hunger_token': NUTRITIVE_VALUE,
                'illness_token': int(self.rotten)
                })

    def updateRotten(self) -> None:
        rand = np.random.random()
        if rand >= self.rotten_chance:
            self.rotten = True


if __name__ == "main":
    pass
