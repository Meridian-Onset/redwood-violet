# redwood-violet 🌳
![Tests](https://github.com/Meridian-Onset/redwood-violet/actions/workflows/tests.yml/badge.svg) ![Monthly Contributions](https://img.shields.io/github/commit-activity/m/Meridian-Onset/redwood-violet?label=Commit%20Activity&logo=Github&logoColor=lightgray) ![Contributor Covenant](https://img.shields.io/badge/Contributor%20Covenant-2.1-4baaaa.svg)


The intention behind this library is to serve as a modular, behavioural simulations library. 

## Components

The library consists of a number of components. The top-level componenent is the `ensemble`. 

### The Ensemble

The ensemble class is an instance of a simulation and is the top-level container for all the other componenents of the simulation. Methods in this class deal with advancing the time-step of the simulation as well as passing information between the actors and the environment. 

The base `Ensemble` class serves as the scaffolding for implementation of arbitrary day-night cycles and reward and punishment initialization. 

Visualization is baked into the base class and is accessible through the `Display_Config` and various animate methods  (`animation_init`, `animate`, etc.) This functionality is implemented using matplotlib, although the idea is to move away from this framework in the future.

## The Environment

The `environment` classes contain all the information about the topology of the simulation.

## Actors

Actor classes represent the behavioral agents in each simulation. `Basic_Actor` is the base class and contains the machinery required to make pseudo-random movements and obervations about it's immediate environment. 

## Simulation State

`src/configuration/cfg.json` contains the parameters of the simulation. Each one can be varied for different effects. 

> Note that when adding new features to an extension of a class, all new variables should be added to this file.

The long-term plan is to add a visual interface that allows the user to change the parameters with greater ease and centrality.
