# redwood-violet 🌳
![Tests](https://github.com/Meridian-Onset/redwood-violet/actions/workflows/tests.yml/badge.svg) ![Monthly Contributions](https://img.shields.io/github/commit-activity/m/Meridian-Onset/redwood-violet?label=Commit%20Activity&logo=Github&logoColor=lightgray) ![Contributor Covenant](https://img.shields.io/badge/Contributor%20Covenant-2.1-4baaaa.svg) [![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)


The intention behind this library is to serve as a modular, behavioral simulation library.

**What is a behavioral simulation?**

A behavioral simulation is a simulation of a group of agents with varying characteristics. The characteristics that can vary between each agent or groups of agents include:

- Physiological:
  - Range of sight
  - Olfactory senses
  - Movement speed
- Behavioral/Psychological, for example:
  - Family structures
  - Sharing and caring
  - Resting tendencies (e.g. nocturnal)

In addition to variations between actors, the environment also changes. Which can lead to advantages or disadvantages for different traits that can be documented.

**Why are behavioral simulations interesting?**

In comparing the evolution of various quantities, like population of competing groups, over large periods of time, we can potentially see how/why certain characteristics emerged during human/more general evolution.

Having said that, this software is not intended as a means to simulate the entirety of evolution, but rather to compare the advantages of certain traits in particular environments between small numbers of differing populations.

*Please note* that this project was, in part, inspired by the work of the creator of [Primer](https://www.youtube.com/channel/UCKzJFdi57J53Vr_BkTfN3uQ).

The hope for the open-source nature of this repository is that you and others use the framework already laid out as inspiration to ask your own questions.

Using the library, you can create your own custom simulations and share them with the community. Reusable parts of your simulation should be integrated into the main library for others to use

# Installation
>Note that this setup procedure assumes that you have Python (>3.7) installed and accessible via either the `python3` or `python` commands in your CLI

Start by cloning the GH repo to local directory with

`git clone git@github.com:Meridian-Onset/redwood-violet.git`

Next we want to create a virtual environment in which we can run the library in editable mode. To do this, navigate to the repository and create a sub-directory called `.venv`. Now run the following commands in your terminal

- `cd .venv` (from main directory)
- `python3 -m venv dev-env`

Next, if on Windows, run the following:
`dev-env\Scripts\activate.bat` (change the `.bat` to `.ps1` if using powershell)

On UNIX or macOS, run this instead:
`source dev-env/bin/activate`

You should now see that your terminal shows `(dev-env)` at the beginning of the command line, meaning that your development environment is ready.

**Note:** To verify that your development environment has been successfully created, run the following two commands and verify that their output paths point to your virtual environment path
1. `pip -V` (note the capital V)
2. `which python`

Next we run the preliminary installation commands (in the main directory):

- `pip install -r requirements_dev.txt`
- `pip install -e .`

The second command installs the library in editable mode, which is necessary for development.

If you'd like to find out more about contributing to this project, consult the `CONTRIBUTING.md` file.



## Components

The library consists of a number of components. The top-level component is the `ensemble`.

### The Ensemble

The ensemble class is an instance of a simulation and is the top-level container for all the other components of the simulation. Methods in this class deal with advancing the time-step of the simulation as well as passing information between the actors and the environment.

The base `Ensemble` class serves as the scaffolding for implementation of arbitrary day-night cycles and reward and punishment initialization.

Visualization is baked into the base class and is accessible through the `Display_Config` and various animate methods (`animation_init`, `animate`, etc.) This functionality is implemented using matplotlib, although the idea is to move away from this framework in the future.

## The Environment

The `environment` classes contain all the information about the topology of the simulation.

## Actors

Actor classes represent the behavioral agents in each simulation. `Basic_Actor` is the base class and contains the machinery required to make pseudo-random movements and obervations about its immediate environment.

## Simulation State

`src/configuration/cfg.json` contains the parameters of the simulation. Each one can be varied for different effects.

> Note that when adding new features to an extension of a class, all new variables should be added to this file.

The long-term plan is to add a visual interface that allows the user to change the parameters with greater ease and centrality.

# Testing
This library uses a combination of the following for running tests:
- **pytest**: for running the custom tests contained in the `tests` directory
- **flake8**: for enforcing the style guide
- **mypy**: for static type checking

Whenever you push to GitHub or create a pull request, a workflow is triggered that uses **tox** to run the tests in a testing environment on Windows, macOS and Linux.

To run the tests indiviually locally, you can use the following commands in the root directory.
- `pytest`
- `flake8 src`
- `mypy src`

Passing each of these tests locally indicates that the github build should pass the tests, unless there's an OS or python version-specific issue which tox will detect. **Tox** can also be invoked locally with the `tox` command.

## Adding Tests

When you'd like to write a new test, either add it to an existing test file under `tests` or create a new appropriately named test file.

The naming of the test files should indicate the nature of the tests. For example, the `test_initialization.py` file contains tests that ensure that each possible ensemble initializes and behaves as expected.
