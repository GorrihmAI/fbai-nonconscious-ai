import numpy as np
from . import config

# Use a fixed input dimension for simplicity in this standalone file
INPUT_DIM = 10 

class AnalogNode:
    """
    Simulates a dissipative analog neuron.
    Strictly stateless between time steps.
    """
    def __init__(self, node_id):
        self.node_id = node_id
        self.state = 0.0
        self.weights = np.random.rand(INPUT_DIM) * 0.1
        
    def activate(self, input_signal):
        # Dissipate previous state immediately
        self.state *= config.DECAY_RATE 
        
        # Ensure input matches weight dimension (simple padding/cutting if needed)
        if len(input_signal) != len(self.weights):
            # Adjust for demo purposes if input size varies
            min_len = min(len(input_signal), len(self.weights))
            potential = np.dot(input_signal[:min_len], self.weights[:min_len])
        else:
            potential = np.dot(input_signal, self.weights)
        
        # Thresholding
        if potential > config.THRESHOLD:
            self.state = potential - config.THRESHOLD
        else:
            self.state = 0.0
            
        return self.state   