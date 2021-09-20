import numpy as np
from enum import Enum, auto
import json
from typing import Iterable
from collections.abc import Iterable

# Import internal modules
from Rewards import Instance
from positions import PositionUnboundedError, Vector_2D

class Basic_Actor:
    #Basic, short_sighted actor without complex behaviours

    def __init__(self, field_size: int):

        x = np.random.random() * field_size
        y = np.random.random() * field_size
        self.position = Vector_2D(x, y)
        self.stats = {'hunger' : 0,
                      'illness' : 0}
        self.found_food = {
            'found_flag' : 0,#Boolean if found
            'finding_position' : Vector_2D(0,0) # Default position
        }
        # TODO: Move these into config files!
        self.move_magnitude = 1
        self.sight_radius = 1

    def __str__(self):
        print(self.position)
        print([f"{key} : {self.stats[key]}" for key in self.stats.keys()])

    def detect_rewards(self, reward_array: Iterable[Instance], print_result: bool=False) -> Vector_2D:
        rewards_in_range = []

        for reward in reward_array:
            # TODO: Check numpy library to clean this machinery up
            dist = (self.x - reward.x)**2 + (self.y - reward.y)**2

            if dist <= self.sight_radius**2:
                rewards_in_range.append(reward.position)
                if print_result != False: print("Yoohoo; found some food!")

            else: pass
        return rewards_in_range

    def generate_increment(self)->Vector_2D:
        x_magnitude = self.move_magnitude * (np.random.random() - 0.5)
        y_magnitude = (self.move_magnitude - abs(x_magnitude))*np.sign(np.random.random() - 0.5)

        return Vector_2D(x_magnitude * self.move_magnitude, y_magnitude * self.move_magnitude, allow_out_of_bounds=True)


    def move(self) -> None:
        """Alters the position of the actor in place"""
        if self.found_food['found_flag'] == True:
            reward = self.found_food['finding_position']
            #TODO: This shouldn't be an instantaneous change (original implementation was an edge case where sight radius is equal to move radius). Should change some kind of pointer
            self.x, self.y = reward
            stats_change = reward.consume() # pop the stats out of the reward object
            self.stats['hunger'] += stats_change['hunger_token']
        else :
            increment = self.generate_increment()
            try:
                self.position = self.position + increment
            except PositionUnboundedError as err:
                #TODO: Somehow iterate on increment here. Should be some way to clean this up. 
                #TODO: Alternate case where actor crosses boundary back into the environment on the other side (continuity)
                pass
            
    def verbose(self) -> str:
        pass


if __name__ == "__main__":
    testActor = Basic_Actor(100)
    print(testActor)

