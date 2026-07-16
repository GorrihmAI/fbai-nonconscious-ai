import numpy as np
from .nodes import AnalogNode
from . import config

class FragmentedModule:
    """Represents one isolated processing unit (e.g., Octopus Arm)."""
    def __init__(self, module_id):
        self.module_id = module_id
        # Create 2 layers of nodes
        self.layers = [
            [AnalogNode(f"M{module_id}_L0_N{i}") for i in range(config.NODES_PER_MODULE)],
            [AnalogNode(f"M{module_id}_L1_N{i}") for i in range(config.NODES_PER_MODULE)]
        ]

    def process(self, input_data):
        """Strict feedforward pass."""
        current_signal = input_data
        for layer in self.layers:
            next_signal = []
            for node in layer:
                out = node.activate(current_signal)
                next_signal.append(out)
            current_signal = np.array(next_signal)
        return current_signal

class FBAISystem:
    """The full system with isolated modules and a dumb router."""
    def __init__(self):
        self.modules = [FragmentedModule(i) for i in range(config.NUM_MODULES)]
        
    def route_dumb(self, outputs):
        """Aggregates outputs without integration (concatenation)."""
        return np.concatenate(outputs)

    def run(self, sensory_inputs):
        """Execute one time step."""
        module_outputs = []
        for i, module in enumerate(self.modules):
            if i < len(sensory_inputs):
                out = module.process(sensory_inputs[i])
                module_outputs.append(out)
        
        if not module_outputs:
            return np.array([])
            
        return self.route_dumb(module_outputs)   