import numpy as np
from .network import FBAISystem
from . import config

def run_demo():
    print("Initializing FBAI System (Non-Conscious Architecture)...")
    system = FBAISystem()
    
    # Create dummy sensory inputs for each module
    sensory_inputs = [np.random.rand(config.INPUT_DIM) for _ in range(config.NUM_MODULES)]
    
    print(f"Running simulation with {config.NUM_MODULES} modules...")
    output = system.run(sensory_inputs)
    
    print(f"System Output: {output}")
    print("Simulation complete. State reset (memory wiped).")

if __name__ == "__main__":
    run_demo()   