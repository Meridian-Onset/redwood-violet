import numpy as np
# from enum import Enum, auto
from typing import Iterable, List

# Import internal modules
from sim_components.Rewards import Instance
from sim_components.positions import PositionUnboundedError, Vector_2D


class Basic_Actor:
    # Basic, short_sighted actor without complex behaviours
    index: int
    x: float
    y: float
    position: Vector_2D
    stats: dict[str, float]
    found_food: bool
    rewards_in_sight: dict[int, Instance]

    def __init__(self, index: int, field_size: int):

        x = np.random.random() * field_size
        y = np.random.random() * field_size
        self.position = Vector_2D(x, y)
        self.stats = {'hunger': 0,
                      'illness': 0}
        self.found_food = False
        self.rewards_in_sight = {}
        # TODO: Move these into config files!
        self.move_magnitude = 1
        self.sight_radius = 1

    def __str__(self):
        return(str([f"{key} : {self.stats[key]}" for key in self.stats.keys()]) + '\n' + str(self.position))

    def detect_rewards(self, reward_array: Iterable[Instance], print_result: bool = False) -> List[Vector_2D]:
        rewards_in_range = []

        for reward in reward_array:
            # TODO: Check numpy library to clean this machinery up
            dist = (self.x - reward.position.x)**2 + (self.y - reward.position.y)**2

            if dist <= self.sight_radius**2:
                rewards_in_range.append(reward.position)
                if print_result is not False:
                    print("Yoohoo; found some food!")

            else:
                pass
        return rewards_in_range

    def generate_increment(self) -> Vector_2D:
        x_magnitude = self.move_magnitude * (np.random.random() - 0.5)
        y_magnitude = (self.move_magnitude - abs(x_magnitude))*np.sign(np.random.random() - 0.5)

        return Vector_2D(x_magnitude * self.move_magnitude, y_magnitude * self.move_magnitude, allow_out_of_bounds=True)

    def choose_reward(self) -> int:
        pass

    def move(self) -> None:
        """Alters the position of the actor in place"""
        if self.found_food:
            reward = self.rewards_in_sight[0]  # TODO: The reward selection needs cleaning up, just choose first one for now
            # TODO: This shouldn't be an instantaneous change
            # TODO: (original implementation was an edge case where sight radius is equal to move radius).
            # TODO: Should change some kind of pointer
            self.x, self.y = reward.position
            stats_change = reward.consume()
            self.stats['hunger'] += stats_change['hunger_token']
        else:
            increment = self.generate_increment()
            try:
                self.position = self.position + increment
            except PositionUnboundedError as err:
                # TODO: Somehow iterate on increment here. Should be some way to clean this up.
                # TODO: Alternate case where actor crosses boundary back into the environment on the other side (continuity)
                print(err.bad_positions)

    def verbose(self) -> str:
        pass


if __name__ == "__main__":
    testActor = Basic_Actor(1, 100)
    print(testActor)
