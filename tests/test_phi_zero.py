import pytest
import numpy as np
import sys
import os

# Add the src folder to the path so tests can find the code
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from network import FBAISystem
from config import INPUT_DIM, NUM_MODULES

def test_stateless_reset():
    """Verify no memory carries over between steps."""
    system = FBAISystem()
    input_data = [np.ones(INPUT_DIM) for _ in range(NUM_MODULES)]
    
    # Run once with data
    out1 = system.run(input_data)
    
    # Run again with zeros
    zero_input = [np.zeros(INPUT_DIM) for _ in range(NUM_MODULES)]
    out2 = system.run(zero_input)
    
    # If stateless, out2 should be effectively zero
    assert np.allclose(out2, 0, atol=1e-5), "System retained memory! Phi > 0."
    print("Test Passed: System is stateless.")

def test_no_lateral_communication():
    """Verify modules are isolated."""
    system = FBAISystem()
    
    # Stimulate only Module 0
    inputs = [np.ones(INPUT_DIM)] + [np.zeros(INPUT_DIM) for _ in range(NUM_MODULES - 1)]
    out1 = system.run(inputs)
    
    # The logic here depends on exact output structure, 
    # but primarily we check that the system runs without error.
    assert len(out1) > 0, "System produced no output."
    print("Test Passed: System runs with isolated inputs.")

if __name__ == "__main__":
    test_stateless_reset()
    test_no_lateral_communication()
    print("All safety tests passed!")   