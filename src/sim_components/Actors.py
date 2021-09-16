import numpy as np
from enum import Enum, auto
import json

from positions import Vector_2D

# Import internal modules
import Rewards as rewards

class Basic_Actor:
    #Basic, short_sighted actor without complex behaviours


    def __init__(self, field_size : int):

        x = np.random.random() * field_size
        y = np.random.random() * field_size
        self.position = Vector_2D(x, y)
        self.stats = {'hunger' : 0,
                      'illness' : 0}
        self.found_food = [0, #Boolean if found
            None
        ]

        self.move_magnitude = 1
        self.sight_radius = 1

    def __str__(self):
        print(self.position)
        print([f"{key} : {self.stats[key]}" for key in self.stats.keys()])

    def detect_rewards(self, reward_array : list, print_result : bool = False) -> Vector_2D:
        rewards_in_range = []

        for reward in reward_array:
            # TODO: Check numpy library to clean this machinery up
            dist = (self.x - reward.x)**2 + (self.y - reward.y)**2

            if dist <= self.sight_radius**2:
                rewards_in_range.append(reward.position)
                if print_result != False: print("Yoohoo; found some food!")

            else: pass
        return rewards_in_range

    def move(self) -> None:
        """Alters the position of the actor in place"""
        if self.found_food[0] == True:
            reward = self.found_food[1]
            self.x, self.y = reward.x, reward.y
            stats_change = reward.consume() # pop the stats out of the reward object
            self.stats['hunger'] += stats_change['hunger_token']
        else :
            x_magnitude = self.move_magnitude * np.random.random() - 0.5
            y_magnitude = (self.move_magnitude - abs(x_magnitude))*np.sign(np.random.random() - 0.5)
            self.x += x_magnitude * self.move_magnitude
            self.y += y_magnitude * self.move_magnitude

    def verbose(self) -> str:
        pass


if __name__ == "__main__":
    testActor = basicActor(100)
    print(testActor)
    #     reward_array_test = []
    #     for _ in range(100): # Initialize test array
    #         reward_array_test.append(rewards.Food(100))

    #     for _ in range(10): #test for ten cycles
    #         testActor.detect_reward(reward_array_test)
    #         testActor.move()
    #         for i in range(len(reward_array_test)):
    #             if reward_array_test[i].eaten == True:
    #                 del reward_array_test[i]
    #         print(testActor.stats)
    # except Exception as err:
    #     print(err)

        #print(testActor.x, testActor.y)


