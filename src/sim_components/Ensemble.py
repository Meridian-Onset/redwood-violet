import numpy as np
import matplotlib.pyplot as plt

import logging
import colorama

import environments as envs
import Actors as actors
import Rewards as rewards
import progressbar as pg
from configuration.config import conf as cfg



np.random.seed(cfg["seed"]) #dank

class InvalidObjectError(Exception):
    def __init__(self, message):
        print(message)

class Ensemble:
    '''Generic ensemble, container for all the machinery of simulations.'''
    field_size = cfg["field_size"]

    def __init__(self, actor_type, num_actors, reward_type = rewards.Instance, reward_scarcity = 0.5, day_night = True):
        #Structure for day-night machinery
        self.day = 0 #day counter
        self.dailyEpochs = {1 : 'Day', 2 : 'Night'} #TODO: add variability for day_night parameter

        #Build simulation terrain
        self.Environment = envs.environment(*[self.field_size]*2)

        #Initiate actors and rewards
        self.players = list()
        for i in range(num_actors):
            self.players.append(actor_type(self.field_size))
        self.reward_scarcity = reward_scarcity

        self.rewards = [reward_type(self.field_size) for i in range(int(self.reward_scarcity * num_actors))]

        #Set `Ensemble` specfic documentation path
        self.docPath = '../docs/Ensemble.md'

    '''        self.rewards = list()
        for i in range(int(self.reward_scarcity * num_actors)):
            self.rewards.append(reward_type(self.field_size))
    '''


    def toArray(self, objects_type) -> list:
        '''Return the x and y coordinates, as arrays, of the specified simulation objects'''
        # TODO: Implement acceptable keywords with
        valids = ("actors", "rewards", "agents", "incentives")
        x, y = np.array([]), np.array([])

        if objects_type.lower() in ('actors', 'agents'):
            array_length = len(self.players)
            x, y = np.empty(array_length), np.empty(array_length)
            for i, player in enumerate(self.players):
                x[i], y[i] = player.position

        elif objects_type.lower() in ("rewards", "incentives"):
            array_length = len(self.rewards)
            x, y = np.empty(array_length), np.empty(array_length)
            for i, reward in enumerate(self.rewards):
                x[i], y[i] = reward.x, reward.y

        else: raise InvalidObjectError(f"Not a valid object type, use one of the following: \n {valids}")
        return[x, y]

    def start(self, cycles : int, buildVideo = False) -> None:
        #TODO:
        '''Main simulation machinery'''
        i = 0 #progress counter
        for _ in range(cycles):

            #TODO: Add day-night functionality
            #i += 1
            #update_progress(i/cycles, operation)

            for actor in self.players:
                actor.move()


    def Display_Config(self, save : bool = False, *args, **kwargs) -> None:
        fig, ax = self.Environment.plot(self.Environment.terrain)

        actor_x, actor_y = self.toArray("actors")
        reward_x, reward_y = self.toArray("rewards")

        #Draw the actors.
        ax.scatter(
            actor_x, actor_y,
            marker = cfg.actorPlottingcfgig['marker'],
            color = cfg.actorPlottingcfgig['color'],
            label = cfg.actorPlottingcfgig['label']
        )

        #Draw the rewards
        ax.scatter(
            reward_x, reward_y,
            marker = cfg.foodPlottingcfgig['marker'],
            color = cfg.foodPlottingcfgig['color'],
            label = cfg.foodPlottingcfgig['label']
        )
        #ax.scatter(reward_x, reward_y, 'bx')
        plt.legend(
            bbox_to_anchor=(0., 1.02, 1., .102), loc=3,
            ncol=2, mode="expand", borderaxespad=0.
            )

        if save: plt.savefig(f'Snapshots/{input("Enter destination filename")}.png')
        plt.show()

    def animation_init(self) -> None:
        #Draws the background environment and starting actors
        fig, ax = self.Environment.plot()

    def animate(self, fig, ax) -> None:
        pass
        #Draws changed

    # ! In Progress
    def documentation(self, externalWindow : bool = True) -> None:
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
    ensembletest = Ensemble(actors.Basic_Actor, 10)
    # #a, b = ensembletest.toArray("actors")
    # #c, d = ensembletest.toArray("rewards")
    # #print(a, b, c, d)
    logging.info('This is an info log')
    ensembletest.Display_Config()
