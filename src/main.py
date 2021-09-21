"""Main entrypoint into simulation library"""

# import logging

import sim_components.Actors as actors

import_all = dict([(name, cls) for name, cls in actors.__dict__.items()])

if __name__ == "__main__":
    print(import_all)
