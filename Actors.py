import numpy as np

import Rewards as rewards

class basicActor:
    #Basic, short_sighted actor without complex behaviours
    
    def __init__(self, field_size): 
        self.x = np.random.random() * field_size
        self.y = np.random.random() * field_size
        self.pos = np.array([self.x, self.y]) #NOTE Currently not in use
        self.stats = {'hunger' : 0,
                      'illness' : 0}
        self.found_food = [0, 0, 0]
        
        self.move_magnitude = 1
        self.sight_radius = 1
        
    def detect_reward(self, reward_array, print_result = False):
        for reward in reward_array:
            #TODO: Check numpy library to clean this machinery up
            dist = np.sqrt((self.x - reward.x)**2 + (self.y - reward.y)**2)
            if dist <= self.sight_radius: 
                self.found_food = [1, reward]
                if print_result != False: print("Yoohoo; found some food!")
                return()
            else: pass
               
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
    testActor = basicActor(100)
    
    reward_array_test = []
    for _ in range(1000):
        reward_array_test.append(rewards.Food(100))
    
    print(reward_array_test)
    for _ in range(10):
        testActor.detect_reward(reward_array_test, print_result = True)
        testActor.move()
        for i in range(len(reward_array_test)):
            if reward_array_test[i].eaten == True: reward_array_test.pop(reward_array_test[i])
        print(testActor.x, testActor.y)   
            
        
        