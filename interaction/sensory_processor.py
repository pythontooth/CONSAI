import numpy as np
from collections import defaultdict

class SensoryProcessor:
    """Processes and integrates multiple sensory inputs."""
    
    def __init__(self):
        self.sensory_buffers = defaultdict(list)
        self.processing_weights = {
            'visual': 0.3,
            'auditory': 0.3,
            'proprioceptive': 0.2,
            'tactile': 0.2
        }
        self.attention_threshold = 0.6
        
    def process_input(self, sensory_data):
        """Process incoming sensory data."""
        processed_data = {}
        
        for modality, data in sensory_data.items():
            if modality in self.processing_weights:
                # Preprocess based on modality
                processed = self._preprocess_modality(modality, data)
                # Apply attention filter
                salience = self._calculate_salience(processed)
                
                if salience >= self.attention_threshold:
                    processed_data[modality] = {
                        'data': processed,
                        'salience': salience,
                        'timestamp': np.datetime64('now')
                    }
                    
                    # Update sensory buffer
                    self.sensory_buffers[modality].append(processed_data[modality])
                    
                    # Maintain buffer size
                    if len(self.sensory_buffers[modality]) > 100:
                        self.sensory_buffers[modality].pop(0)
        
        return processed_data
    
    def _preprocess_modality(self, modality, data):
        """Preprocess data based on sensory modality."""
        if modality == 'visual':
            return self._process_visual(data)
        elif modality == 'auditory':
            return self._process_auditory(data)
        return data
    
    def _process_visual(self, data):
        """Process visual input."""
        # Placeholder for visual processing
        return {'type': 'visual', 'processed_data': data}
    
    def _process_auditory(self, data):
        """Process auditory input."""
        # Placeholder for auditory processing
        return {'type': 'auditory', 'processed_data': data}
    
    def _calculate_salience(self, data):
        """Calculate salience of processed data."""
        # Placeholder for salience calculation
        return np.random.uniform(0.5, 1.0)
