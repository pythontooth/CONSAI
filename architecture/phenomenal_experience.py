import numpy as np
from collections import OrderedDict

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
        # This is a simplified simulation of how content might map to experience
        
        # Conceptual processing - all content affects understanding
        self.qualia_dimensions["conceptual"]["understanding"] += 0.5
        self.qualia_dimensions["conceptual"]["meaning"] += np.random.uniform(0.3, 0.7)
        
        # Content-specific processing based on identifiers
        if isinstance(content_id, str):
            if "visual" in content_id:
                self.qualia_dimensions["visual"]["color_intensity"] += 0.8
                self.qualia_dimensions["visual"]["spatial_structure"] += 0.7
            elif "emotion" in content_id:
                self.qualia_dimensions["emotional"]["valence"] += np.random.uniform(-1.0, 1.0)
                self.qualia_dimensions["emotional"]["arousal"] += np.random.uniform(0.0, 1.0)
            elif "time" in content_id or "memory" in content_id:
                self.qualia_dimensions["temporal"]["duration_perception"] += 0.6
                self.qualia_dimensions["temporal"]["sequence_awareness"] += 0.8
        
        # Cap values at 1.0
        for category in self.qualia_dimensions.values():
            for dimension in category:
                category[dimension] = min(category[dimension], 1.0)
    
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
