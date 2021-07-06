import numpy as np
import matplotlib.pyplot as plt

import Actors as actors
import Rewards as rewards
import config as conf
import progressbar as pg


np.random.seed(conf.seed) #dank

class InvalidObjectError(Exception):
    pass

class Ensemble:
    
    field_size = conf.field_size
    
    def __init__(self, actor_type, num_actors, reward_type = rewards.Food, reward_scarcity = 0.5, day_night = True):
        #Structure for day-night machinery
        self.day = 0 #day counter
        self.dailyEpochs = {1 : 'Day', 2 : 'Night'} #TODO: add variability for day_night parameter
        
        #Initiate actors and rewards
        self.players = list()
        for i in range(num_actors):
            self.players.append(actor_type(self.field_size))
        self.reward_scarcity = reward_scarcity
        self.rewards = list()
        for i in range(int(self.reward_scarcity * num_actors)):
            self.rewards.append(reward_type(self.field_size))
        
        #Set `Ensemble` specfic documentation path
        self.docPath = '../docs/Ensemble.md'
    
    def toArray(self, objects_type):
        '''Return the x and y coordinates, as arrays, of the specified simulation objects'''
        valids = ("actors", "rewards", "agents", "incentives")
        x, y = np.array([]), np.array([])
            
        if objects_type.lower() in ('actors', 'agents'): 
            array_length = len(self.players)
            x, y = np.empty(array_length), np.empty(array_length)
            for i, player in enumerate(self.players):
                x[i], y[i] = player.x, player.y
                
        elif objects_type.lower() in ("rewards", "incentives"):
            array_length = len(self.rewards)
            x, y = np.empty(array_length), np.empty(array_length)
            for i, reward in enumerate(self.rewards):
                x[i], y[i] = reward.x, reward.y
        
        else: raise InvalidObjectError(f"Not a valid object type, use one of the following: \n {valids}")
        return(x, y)
    
    def start(self, cycles : int, buildVideo = False):
        #TODO: 
        '''Main simulation machinery'''
        i = 0 #progress counter
        for _ in range(cycles):
            
            #TODO: Add day-night functionality
            i += 1
            update_progress(i/cycles, operation)
            for actor in self.players:
                actor.move()
                
        
    def DisplayConfig(self, save = False, *args, **kwargs):
        fig = plt.Figure()
        actor_x, actor_y = self.toArray("actors")
        reward_x, reward_y = self.toArray("rewards")
        plt.plot(actor_x, actor_y, 'rx', reward_x, reward_y, 'bx')
        plt.legend()
        plt.show()
            
    def documentation(self, externalWindow = True):
        '''Function that displays the full documentation for explaining the use and implementation of the class'''
        #TODO: Write the segment that opens the markdown file viewer
        try:
            with open(self.docPath, 'r') as f:
                docText = f.read()
        except FileNotFoundError:
            print('Documentation missing, check integrity of filesystem')
            
class DependentFoodScarcityEnsemble(Ensemble):
    #TODO: Write this class that has the food scarcity change depending on the amount of food leftover
    #the previous day
    def __init__(self):
        return('butts')
    
if __name__ == "__main__":
    ensembletest = Ensemble(actors.basicActor, 10)
    ensembletest.DisplayConfig()