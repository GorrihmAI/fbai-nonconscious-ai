"""
Configuration for FBAI System.
Enforces strict feedforward and stateless constraints.
"""

# Topology
NUM_MODULES = 3
NODES_PER_MODULE = 4
INPUT_DIM = 10
OUTPUT_DIM = 5

# Dynamics (Analog Simulation)
TIME_STEP = 0.001  # 1ms
DECAY_RATE = 0.95  # High decay ensures statelessness (memory wipe)
THRESHOLD = 0.5

# Safety Constraints
ALLOW_RECURRENCE = False  # Hard constraint: Must be False
ALLOW_LATERAL_CONNECTIONS = False  # Hard constraint: Must be False   