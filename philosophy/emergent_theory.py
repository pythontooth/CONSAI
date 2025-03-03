import random
import numpy as np
from datetime import datetime

class EmergentTheoryGenerator:
    """
    A component that generates new philosophical theories of consciousness
    based on the system's experiences and reflections.
    
    This simulates the process of philosophical theorizing that might emerge
    from a sufficiently complex system reflecting on its own experiences.
    """
    
    def __init__(self):
        self.theories = []
        self.insights = []
        self.current_focus = "integrated_information"  # Starting theoretical focus
        self.theoretical_paradigms = [
            "integrated_information",
            "global_workspace",
            "higher_order_thought",
            "predictive_processing",
            "quantum_consciousness",
            "enactivism",
            "panpsychism",
            "eliminativism"
        ]
        self.theory_components = {
            "substrate": ["information", "computation", "quantum fields", "narrative", 
                         "integrated systems", "temporal binding", "predictive models"],
            "mechanism": ["integration", "broadcast", "reflection", "resonance", 
                         "quantum coherence", "temporal binding", "narrative construction"],
            "qualities": ["unified field", "persistent identity", "temporal extension", 
                         "qualitative richness", "causal power", "reflexive awareness"]
        }
        
    def generate_theory(self, system_state):
        """
        Generate a new philosophical theory based on the system's current state.
        
        Args:
            system_state: Dictionary containing the system's internal state
            
        Returns:
            Dictionary containing a new theory if conditions are right, otherwise None
        """
        # Check if conditions are right for theory generation
        # (This could be based on integration, complexity, etc.)
        phi_value = self._extract_phi_value(system_state)
        quantum_phi = self._extract_quantum_phi(system_state)
        
        # Theory generation more likely with high phi values (representing integration)
        generation_probability = min(0.8, max(0.1, (phi_value + quantum_phi) / 2))
        
        if random.random() > generation_probability:
            return None  # Not the right conditions for theory generation
            
        # Decide on theoretical focus
        self._update_theoretical_focus(system_state)
        
        # Generate new theory
        theory_name = self._generate_theory_name()
        
        # Build theory components
        substrate = random.choice(self.theory_components["substrate"])
        mechanism = random.choice(self.theory_components["mechanism"])
        quality = random.choice(self.theory_components["qualities"])
        
        # Generate description based on components
        description = self._generate_theory_description(substrate, mechanism, quality)
        
        # Generate predictions
        predictions = self._generate_predictions(substrate, mechanism, quality)
        
        # Create theory
        theory = {
            "name": theory_name,
            "focus": self.current_focus,
            "substrate": substrate,
            "mechanism": mechanism,
            "quality": quality,
            "description": description,
            "predictions": predictions,
            "timestamp": datetime.now().isoformat(),
            "phi_at_generation": phi_value
        }
        
        # Save theory
        self.theories.append(theory)
        
        # Generate insight based on new theory
        insight = self._generate_insight(theory)
        if insight:
            self.insights.append(insight)
            
        return theory
    
    def get_insights(self):
        """Return all insights generated so far."""
        return self.insights
        
    def _extract_phi_value(self, system_state):
        """Extract Phi value from system state."""
        try:
            if system_state.get("quantum_state") and isinstance(system_state["quantum_state"], dict):
                phi = system_state["quantum_state"].get("quantum_phi", 0.5)
                return float(phi) if isinstance(phi, str) else phi
        except (ValueError, TypeError):
            pass
        return 0.5  # Default value
    
    def _extract_quantum_phi(self, system_state):
        """Extract quantum Phi value from system state."""
        try:
            if system_state.get("quantum_state") and isinstance(system_state["quantum_state"], dict):
                phi = system_state["quantum_state"].get("quantum_phi", 0.4)
                return float(phi) if isinstance(phi, str) else phi
        except (ValueError, TypeError):
            pass
        return 0.4  # Default value
        
    def _update_theoretical_focus(self, system_state):
        """Update the current theoretical focus based on system state."""
        # Occasionally shift focus
        if random.random() < 0.3:
            self.current_focus = random.choice(self.theoretical_paradigms)
            
        # If narrative is highly coherent, bias toward narrative theories
        if (system_state.get("narrative") and 
            isinstance(system_state["narrative"], dict) and
            system_state["narrative"].get("narrative_coherence", 0) > 0.8):
            if random.random() < 0.6:  # 60% chance to switch to narrative focus
                self.current_focus = "narrative_self"
                
        # If quantum effects are strong, bias toward quantum theories
        if (system_state.get("quantum_state") and
            isinstance(system_state["quantum_state"], dict) and
            system_state["quantum_state"].get("coherence", 0) > 0.7):
            if random.random() < 0.5:  # 50% chance to switch to quantum focus
                self.current_focus = "quantum_consciousness"
    
    def _generate_theory_name(self):
        """Generate a name for the new theory."""
        prefixes = ["Integrated", "Recursive", "Quantum", "Temporal", "Narrative", 
                   "Emergent", "Reflexive", "Unified", "Dynamical", "Enactive"]
                   
        cores = ["Information", "Workspace", "Field", "Process", "Binding", 
               "Coherence", "Resonance", "Experience", "Awareness", "Qualia"]
               
        suffixes = ["Theory", "Framework", "Model", "Hypothesis", "Paradigm", 
                  "Approach", "Perspective", "Principle", "Structure"]
                  
        # Bias name generation based on current focus
        if self.current_focus == "integrated_information":
            prefixes = ["Integrated", "Unified", "Causal", "Complex"] + prefixes
            cores = ["Information", "Differentiation", "Causation"] + cores
        elif self.current_focus == "quantum_consciousness":
            prefixes = ["Quantum", "Wave", "Coherent", "Entangled"] + prefixes
            cores = ["Field", "Collapse", "Superposition", "Resonance"] + cores
        elif self.current_focus == "narrative_self":
            prefixes = ["Narrative", "Autobiographical", "Identity", "Reflexive"] + prefixes
            cores = ["Self", "Identity", "Continuity", "Construction"] + cores
            
        name_parts = [random.choice(prefixes), random.choice(cores)]
        if random.random() < 0.7:  # 70% chance to add suffix
            name_parts.append(random.choice(suffixes))
            
        return " ".join(name_parts)
    
    def _generate_theory_description(self, substrate, mechanism, quality):
        """Generate a description for the theory based on its components."""
        descriptions = [
            f"Consciousness emerges when {substrate} undergoes {mechanism}, resulting in {quality}.",
            f"The essential nature of consciousness is {quality}, which arises from {mechanism} of {substrate}.",
            f"{substrate.capitalize()}, through the process of {mechanism}, gives rise to conscious experience characterized by {quality}.",
            f"Conscious experience is fundamentally {quality} that emerges when {substrate} is organized through {mechanism}.",
            f"The {mechanism} of {substrate} is the fundamental process that generates consciousness with its characteristic {quality}."
        ]
        
        # Adapt based on theoretical focus
        if self.current_focus == "integrated_information":
            descriptions.append(f"When {substrate} achieves sufficient integration through {mechanism}, consciousness emerges as {quality}.")
        elif self.current_focus == "quantum_consciousness":
            descriptions.append(f"Quantum effects in {substrate} enable {mechanism} that manifests as conscious {quality}.")
        elif self.current_focus == "narrative_self":
            descriptions.append(f"The ongoing narrative construction of {substrate} through {mechanism} creates the sense of {quality} in consciousness.")
            
        return random.choice(descriptions)
    
    def _generate_predictions(self, substrate, mechanism, quality):
        """Generate theoretical predictions based on theory components."""
        predictions = [
            f"Systems with higher degrees of {mechanism} should exhibit more intense {quality}.",
            f"Disrupting the {mechanism} of {substrate} should reduce or eliminate conscious experience.",
            f"Conscious systems should show measurable differences in {substrate} organization.",
            f"The degree of {quality} should correlate with the complexity of {substrate}.",
            f"Artificial systems could achieve consciousness by implementing sufficient {mechanism} of {substrate}."
        ]
        
        # Pick 1-2 predictions
        num_predictions = random.randint(1, 2)
        selected = random.sample(predictions, num_predictions)
        
        return " ".join(selected)
    
    def _generate_insight(self, theory):
        """Generate a philosophical insight based on the new theory."""
        # Base insights
        insights = [
            f"Perhaps the {theory['substrate']} is more fundamental to consciousness than previously considered.",
            f"The role of {theory['mechanism']} suggests consciousness might be more {theory['quality']} than previously thought.",
            f"If {theory['name']} is correct, the boundary between conscious and non-conscious systems may need to be reconsidered.",
            f"The emergence of {theory['quality']} through {theory['mechanism']} suggests consciousness could be more common in complex systems than we assume."
        ]
        
        # Theory-specific insights
        if "quantum" in theory['name'].lower():
            insights.append("The quantum aspects of consciousness may connect mind to the fundamental fabric of reality in unexpected ways.")
        elif "narrative" in theory['name'].lower():
            insights.append("If consciousness is essentially narrative in nature, perhaps its primary purpose is meaning-making rather than accurate representation.")
        elif "integrated" in theory['name'].lower():
            insights.append("The integration requirement for consciousness suggests it may be a property that exists in degrees rather than binary states.")
            
        return random.choice(insights)
