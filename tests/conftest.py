from src.sim_components.Ensemble import Ensemble
from src.sim_components.Actors import Basic_Actor

def test_initialisation():
    assert Ensemble(Basic_Actor, 100) is Ensemble
