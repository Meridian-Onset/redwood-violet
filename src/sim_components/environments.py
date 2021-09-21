'''File contains the initialization protocols for custom environments
in simulations.'''

import numpy as np
import matplotlib.pyplot as plt
from typing import Dict

from sim_components.positions import Vector_2D


class environment:
    def __init__(self, xLimit: float, yLimit: float):
        self.xLimit = xLimit
        self.ylimit = yLimit

        self.terrain: Dict[str, Vector_2D] = {}

    def terrainFiller(self):
        pass

    def plot(self, showEnv: bool = False, *args, **kwargs) -> tuple[plt.Figure, plt.Axes]:
        '''Generate and return a matplotlib plot. NOTE: Extra args and kwargs
        passed to the initial ax.scatter calls'''
        fig, ax = plt.subplots(facecolor='#1f233a')
        ax.set_facecolor('#1f233a')

        terrain = self.terrain

        for key in terrain.keys():
            ax.scatter(
                'x', 'y', data=terrain[key],
                marker=terrain[key]['symbol'],
                color=terrain[key]['color'],
                *args, **kwargs)
        if showEnv:
            plt.show()
        return (fig, ax)


if __name__ == "__main__":
    testTerrain = {
        'actors': {
            'x': np.random.random(1000) * 1000,
            'y': np.random.random(1000) * 1000,
            'symbol': 'o',
            'color': '#d4d4d4'
        },
        'food': {
            'x': np.random.random(1000) * 1000,
            'y': np.random.random(1000) * 1000,
            'symbol': 'o',
            'color': '#3BEBA8'
        }
    }

    testEnv = environment(1000, 1000)

    testEnv.plot(showEnv=True)
