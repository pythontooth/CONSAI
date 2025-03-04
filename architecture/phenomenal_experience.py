import numpy as np
from collections import OrderedDict
import random
import time

class PhenomenalExperience:
    """
    A theoretical module for modeling "what it's like" experiences.
    
    This component attempts to model the qualitative aspects of consciousness
    (qualia) and how they might emerge in an intelligent system.
    """
    
    def __init__(self):
        # Dictionary of "qualia" types the system can model
        self.qualia_dimensions = OrderedDict({
            "visual": {
                "color_intensity": 0.0,
                "spatial_structure": 0.0,
                "object_recognition": 0.0
            },
            "conceptual": {
                "understanding": 0.0,
                "meaning": 0.0,
                "relevance": 0.0
            },
            "emotional": {
                "valence": 0.0,  # negative to positive 
                "arousal": 0.0,   # calm to excited
                "confidence": 0.0  # uncertainty to certainty
            },
            "temporal": {
                "duration_perception": 0.0,
                "sequence_awareness": 0.0
            }
        })
        self.experience_memory = []
        self.max_memories = 100
        
    def simulate_experience(self, workspace_contents):
        """
        Generate a simulated phenomenal experience from current contents.
        
        Args:
            workspace_contents: Dictionary of information in global workspace
            
        Returns:
            A description of the simulated "experience"
        """
        # Reset qualia values
        for category in self.qualia_dimensions.values():
            for dimension in category:
                category[dimension] = 0.0
        
        # Process workspace contents to generate "experience"
        for content_id, content in workspace_contents.items():
            self._process_content_to_qualia(content_id, content)
            
        # Generate experience description based on active qualia
        experience = self._generate_experience_description()
        
        # Store in experience memory
        self._store_experience(experience)
        
        return experience
        
    def _process_content_to_qualia(self, content_id, content):
        """Map content to phenomenal dimensions."""
        # Dynamic selection of number of active categories based on cycle
        cycle_phase = np.sin(self.processing_cycles * 0.1) if hasattr(self, 'processing_cycles') else 0
        base_categories = 2
        extra_categories = 1 if random.random() < (0.3 + cycle_phase * 0.2) else 0
        num_active_categories = base_categories + extra_categories
        
        # Ensure we don't always pick the same categories
        category_weights = {
            "visual": 0.2 + 0.1 * np.sin(time.time()),
            "conceptual": 0.3 + 0.1 * np.cos(time.time()),
            "emotional": 0.2 + 0.1 * np.sin(time.time() * 0.5),
            "temporal": 0.3 + 0.1 * np.cos(time.time() * 0.5)
        }
        
        # Normalize weights
        total_weight = sum(category_weights.values())
        category_weights = {k: v/total_weight for k, v in category_weights.items()}
        
        # Weighted random selection of categories
        active_categories = random.choices(
            list(self.qualia_dimensions.keys()),
            weights=[category_weights[k] for k in self.qualia_dimensions.keys()],
            k=num_active_categories
        )
        
        # Process each category with varying intensities
        for category in self.qualia_dimensions:
            if category in active_categories:
                # Base intensity with temporal variation
                base_intensity = 0.4 + 0.3 * np.sin(time.time() * 0.2)
                # Add random variation
                intensity = base_intensity + random.uniform(-0.2, 0.2)
                
                # Select random number of dimensions to activate
                num_dims = random.randint(1, len(self.qualia_dimensions[category]))
                dimensions = random.sample(list(self.qualia_dimensions[category].keys()), k=num_dims)
                
                for dim in dimensions:
                    # Add some noise to intensity
                    dim_intensity = max(0.1, min(1.0, intensity + random.gauss(0, 0.1)))
                    self.qualia_dimensions[category][dim] = dim_intensity

        # Occasionally add a brief intense experience
        if random.random() < 0.05:  # 5% chance
            cat = random.choice(list(self.qualia_dimensions.keys()))
            dim = random.choice(list(self.qualia_dimensions[cat].keys()))
            self.qualia_dimensions[cat][dim] = random.uniform(0.9, 1.0)
    
    def _generate_experience_description(self):
        """Generate a description of the current phenomenal experience."""
        active_dimensions = []
        
        # Collect strongly activated dimensions (>0.5)
        for category_name, category in self.qualia_dimensions.items():
            for dim_name, value in category.items():
                if value > 0.5:
                    qualifier = "strongly" if value > 0.8 else "moderately"
                    active_dimensions.append(f"{qualifier} experiencing {dim_name} in {category_name} dimension")
        
        if not active_dimensions:
            return "No significant phenomenal experience"
            
        return "I am " + ", and ".join(active_dimensions)
    
    def _store_experience(self, experience):
        """Store experience in memory."""
        self.experience_memory.append(experience)
        if len(self.experience_memory) > self.max_memories:
            self.experience_memory.pop(0)  # Remove oldest
