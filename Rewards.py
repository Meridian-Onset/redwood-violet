import numpy as np
import config as cfg

class Instance:
    '''Standard reward type, no change to actor stats, food and poison inherit from this class''' # TODO : fix this to use the vector class
    def __init__(self, field_size, rotten_chance = 0):
        self.x = np.random.random() * field_size
        self.y = np.random.random() * field_size
        self.rotten_chance = rotten_chance
        self.rotten = (np.random.random() < rotten_chance)
        self.eaten = False
        self.position = cfg.Position(self.x, self.y)

    def consume(self) -> dict:
        """The consume method pops the attribute additives to the consumer."""
        self.eaten = True #value to apply a mask to in ensemble object
        return({
                'hunger_token' : config.food_values['default_nutritive_value'],
                'illness_token' : int(self.rotten)
                })

    def checkRotten(self) -> None:
        rand = np.random.random()
        if rand >= self.rotten_chance:
            self.rotten = True
