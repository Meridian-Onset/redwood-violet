from src.sim_components.Ensemble import Ensemble
from src.sim_components.Actors import Basic_Actor

def test_initialisation():
    # Assert that ensemble initialises correctly and runs all different vanilla methods
    ensemble_for_testing = Ensemble(Basic_Actor, 100)
    assert isinstance(ensemble_for_testing, Ensemble)

    # Test array method
    ensemble_arrays = ensemble_for_testing.toArray('actors')
    assert len(ensemble_arrays) >= 2
    assert len(ensemble_arrays[0]) == 100
    assert len(ensemble_arrays[1]) == 100

    ensemble_for_testing.start(100)
    assert ensemble_for_testing is Ensemble
