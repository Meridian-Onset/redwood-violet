import numpy as np

class Food:
    '''Standard reward type, no change to actor stats other than change hungry status'''
    def __init__(self, field_size, rotten_chance = 0):
        self.x = np.random.random() * field_size
        self.y = np.random.random() * field_size
        self.rotten = (np.random.random() < rotten_chance)
        self.eaten = False
    
    def consume(self):
        self.eaten = True
        return({
                'hunger_token' : 1,
                'illness_token' : int(self.rotten)
                })