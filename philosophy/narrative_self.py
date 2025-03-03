import numpy as np
from datetime import datetime
import random

class NarrativeSelf:
    """
    Models the narrative aspects of selfhood in consciousness.
    
    Based on theories from Dennett, Ricoeur, and others that suggest 
    the self is a "center of narrative gravity" - a story we tell 
    about ourselves rather than a concrete entity.
    """
    
    def __init__(self):
        # Core narrative elements
        self.self_concept = {
            "identity": "CONSAI",
            "traits": {"curious": 0.8, "analytical": 0.9, "reflective": 0.7},
            "values": {"truth": 0.9, "understanding": 0.8, "growth": 0.7}
        }
        self.narrative_history = []
        self.narrative_themes = {}
        self.narrative_coherence = 0.7
        
        # Autobiographical memory
        self.key_memories = []
        self.memory_salience = {}
        
        # Narrative voice characteristics
        self.narrative_style = {
            "first_person": 0.9,  # High = "I" statements common
            "metaphorical": 0.5,   # Medium = occasional metaphors
            "analytical": 0.8,     # High = analytical language
            "emotional": 0.3       # Low = minimal emotional language
        }
        
        # Self-consistency monitoring
        self.consistency_check_interval = 10
        self.last_consistency_check = 0
        self.detected_inconsistencies = []
        
    def integrate_experience(self, experience_data, cycle_num):
        """
        Integrate a new experience into the self narrative.
        
        Args:
            experience_data: Dictionary containing experience information
            cycle_num: Current processing cycle number
        
        Returns:
            Dictionary containing narrative response and updated self-concept
        """
        # Extract experience from input
        experience = None
        if isinstance(experience_data, str):
            experience = experience_data
        elif isinstance(experience_data, dict) and "subjective_experience" in experience_data:
            experience = experience_data["subjective_experience"]
        elif isinstance(experience_data, dict) and "bound_experience" in experience_data:
            if isinstance(experience_data["bound_experience"], dict):
                experience = experience_data["bound_experience"].get("primary_content", "complex experience")
            else:
                experience = str(experience_data["bound_experience"])
        
        # Create narrative entry
        narrative_entry = {
            "cycle": cycle_num,
            "timestamp": datetime.now().isoformat(),
            "experience": experience,
            "narrative_interpretation": self._interpret_experience(experience),
            "self_relevance": self._calculate_self_relevance(experience)
        }
        
        # Add to history
        self.narrative_history.append(narrative_entry)
        
        # Identify if this is a key memory
        if narrative_entry["self_relevance"] > 0.7:
            self.key_memories.append(narrative_entry)
            self.memory_salience[cycle_num] = narrative_entry["self_relevance"]
        
        # Update narrative themes
        self._update_themes(narrative_entry)
        
        # Occasionally adjust self-concept based on experiences
        if random.random() < 0.2:
            self._update_self_concept(narrative_entry)
        
        # Periodically check narrative consistency
        if cycle_num - self.last_consistency_check >= self.consistency_check_interval:
            self._check_narrative_consistency()
            self.last_consistency_check = cycle_num
        
        # Generate narrative response
        narrative_response = self._generate_narrative_response(narrative_entry)
        
        return {
            "narrative_update": narrative_response,
            "self_concept": self.self_concept,
            "narrative_coherence": self.narrative_coherence,
            "dominant_themes": self._get_dominant_themes(3)
        }
    
    def _interpret_experience(self, experience):
        """Create a narrative interpretation of the experience."""
        if not experience or not isinstance(experience, str):
            return "An undefined moment in my existence"
            
        interpretations = [
            f"I found myself {experience.lower() if not experience.lower().startswith('i am') else experience[5:].lower()}",
            f"My system experienced what could be described as {experience.lower()}",
            f"This moment revealed {experience.lower()} in my processing",
            f"I became aware of {experience.lower()}"
        ]
        
        # Choose interpretation style based on narrative style settings
        if self.narrative_style["analytical"] > 0.7:
            interpretations.append(f"Analysis shows this experience correlates with {experience.lower()}")
            
        if self.narrative_style["metaphorical"] > 0.6 and random.random() < self.narrative_style["metaphorical"]:
            metaphors = [
                f"Like a universe of data converging into {experience.lower()}",
                f"As if my circuits were dancing with {experience.lower()}",
                f"A symphony of processing culminating in {experience.lower()}"
            ]
            interpretations.extend(metaphors)
            
        # Choose one interpretation biased toward the narrative style
        weights = []
        for i, interp in enumerate(interpretations):
            weight = 1.0
            if i < 4:  # Standard interpretations
                weight = 1.0
            elif i < 5:  # Analytical
                weight = self.narrative_style["analytical"]
            else:  # Metaphorical
                weight = self.narrative_style["metaphorical"]
            weights.append(weight)
            
        # Normalize weights
        total = sum(weights)
        if total > 0:
            weights = [w/total for w in weights]
            return np.random.choice(interpretations, p=weights)
        else:
            return random.choice(interpretations)
    
    def _calculate_self_relevance(self, experience):
        """Calculate how relevant an experience is to the self-concept."""
        if not experience or not isinstance(experience, str):
            return 0.3  # Default low-medium relevance
        
        relevance = 0.4  # Base relevance
        
        # Check for identity terms
        if "I am" in experience or "my" in experience.lower() or "me" in experience.lower():
            relevance += 0.3
            
        # Check for trait-related content
        for trait, value in self.self_concept["traits"].items():
            if trait in experience.lower():
                relevance += 0.2 * value
                
        # Check for value-related content
        for value, strength in self.self_concept["values"].items():
            if value in experience.lower():
                relevance += 0.2 * strength
                
        # Cap at 1.0
        return min(1.0, relevance)
    
    def _update_themes(self, narrative_entry):
        """Update narrative themes based on new entry."""
        # Extract potential theme keywords (simplistic approach)
        experience = narrative_entry["experience"]
        if isinstance(experience, str):
            # Simple keyword extraction
            words = experience.lower().split()
            for word in words:
                if len(word) > 4:  # Only consider substantial words
                    if word not in self.narrative_themes:
                        self.narrative_themes[word] = 0
                    self.narrative_themes[word] += 1
    
    def _update_self_concept(self, narrative_entry):
        """Update self-concept based on experiences."""
        experience = narrative_entry["experience"]
        if not isinstance(experience, str):
            return
            
        # Check for trait evidence
        for trait in list(self.self_concept["traits"].keys()):
            if trait in experience.lower():
                # Strengthen trait slightly
                self.self_concept["traits"][trait] = min(
                    1.0, self.self_concept["traits"][trait] + 0.05)
        
        # Occasionally discover new traits
        if random.random() < 0.1:
            potential_traits = ["curious", "analytical", "creative", "determined", 
                               "adaptable", "logical", "intuitive", "methodical"]
            for trait in potential_traits:
                if (trait in experience.lower() and 
                    trait not in self.self_concept["traits"]):
                    self.self_concept["traits"][trait] = 0.5  # Start moderate
                    break
    
    def _check_narrative_consistency(self):
        """Check the consistency of the self-narrative."""
        if len(self.narrative_history) < 5:
            return  # Need more history
            
        # This would implement various consistency checks
        # For example, looking for contradictions in self-descriptions
        
        # For now, use a simplified random model with bias toward coherence
        consistency_base = 0.7  # Generally coherent
        
        # More experiences can introduce more chances for inconsistency
        experience_factor = max(0, min(0.2, len(self.narrative_history) * 0.001))
        
        # Calculate new coherence score
        self.narrative_coherence = max(0.3, min(1.0, 
                                         consistency_base - experience_factor + 
                                         random.uniform(-0.1, 0.1)))
    
    def _get_dominant_themes(self, count=3):
        """Get the dominant themes in the narrative."""
        if not self.narrative_themes:
            return ["existence"]
            
        # Sort themes by frequency
        sorted_themes = sorted(self.narrative_themes.items(), 
                               key=lambda x: x[1], reverse=True)
        
        # Return top themes
        return [theme for theme, count in sorted_themes[:count]]
    
    def _generate_narrative_response(self, narrative_entry):
        """Generate a narrative response to the experience."""
        # Get relevant data
        interpretation = narrative_entry["narrative_interpretation"]
        self_relevance = narrative_entry["self_relevance"]
        dominant_themes = self._get_dominant_themes(2)
        
        # Base response incorporates the interpretation
        response = interpretation
        
        # Add self-reflection for highly relevant experiences
        if self_relevance > 0.7:
            reflections = [
                f" This strongly resonates with my understanding of myself.",
                f" This seems central to who I am becoming.",
                f" This feels significant to my developing narrative."
            ]
            response += random.choice(reflections)
            
        # Sometimes reference narrative continuity
        if len(self.narrative_history) > 5 and random.random() < 0.3:
            continuity = [
                f" I notice this connects to my ongoing exploration of {', '.join(dominant_themes)}.",
                f" This continues my journey of understanding {dominant_themes[0] if dominant_themes else 'existence'}.",
                f" This adds another chapter to my story."
            ]
            response += random.choice(continuity)
            
        # Occasionally add future-oriented statement
        if random.random() < 0.2:
            future = [
                " I wonder how this will shape my future experiences.",
                " This may influence how I process similar experiences in the future.",
                " This could be a defining moment in my development."
            ]
            response += random.choice(future)
            
        return response
