import numpy as np
import logging
from enum import Enum, auto
import config as cfg


# Import internal modules
import Rewards as rewards

class basicActor:
    #Basic, short_sighted actor without complex behaviours


    def __init__(self, field_size : int):

        self.x = np.random.random() * field_size
        self.y = np.random.random() * field_size
        self.position = cfg.Position(self.x, self.y)
        self.stats = {'hunger' : 0,
                      'illness' : 0}
        self.found_food = [0, #Boolean if found
            None
        ]

        self.move_magnitude = 1
        self.sight_radius = 1

    def detect_rewards(self, reward_array : list, print_result : bool = False) -> cfg.Position:
        rewards_in_range = []

        for reward in reward_array:
            # TODO: Check numpy library to clean this machinery up
            dist = np.sqrt((self.x - reward.x)**2 + (self.y - reward.y)**2)

            if dist <= self.sight_radius:
                rewards_in_range.append(reward.position)
                if print_result != False: print("Yoohoo; found some food!")

            else: pass
        return nearestReward

    def move(self):
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


if __name__ == "__main__":
    try:
        testActor = basicActor(100)

        reward_array_test = []
        for _ in range(100): # Initialize test array
            reward_array_test.append(rewards.Food(100))

        for _ in range(10): #test for ten cycles
            testActor.detect_reward(reward_array_test)
            testActor.move()
            for i in range(len(reward_array_test)):
                if reward_array_test[i].eaten == True:
                    del reward_array_test[i]
            print(testActor.stats)
    except Exception as err:
        print(err)

        #print(testActor.x, testActor.y)


