from src.sim_components.Ensemble import Ensemble
from src.sim_components.Actors import Basic_Actor

def test_initialisation():
    # Assert that ensemble initialises correctly and runs all different vanilla methods
    ensemble_for_testing = Ensemble(Basic_Actor, 100)
    assert ensemble_for_testing is Ensemble

    # Test array method
    ensemble_arrays = ensemble_for_testing.toArray('actors')
    assert ensemble_arrays.length >= 2
    assert ensemble_arrays[0].length == 100
    assert ensemble_arrays[1].length == 100

    ensemble_for_testing.start(100)
    assert ensemble_for_testing is Ensemble
    