import numpy as np
from datetime import datetime

class SelfReflectionModule:
    """
    Self-reflection component that models the system's ability to 
    reason about its own internal states and processes.
    """
    
    def __init__(self, global_workspace):
        self.global_workspace = global_workspace
        self.self_model = {
            "identity": "CONSAI",
            "purpose": "Exploring theoretical aspects of machine consciousness",
            "capabilities": ["self-reflection", "integrated information processing",
                            "phenomenal experience modeling", "introspection"],
            "history": []
        }
        self.reflection_depth = 0  # Tracks recursive reflection depth
        
    def reflect(self, internal_state, max_depth=3):
        """
        Generate reflective thoughts about the system's current state.
        
        Args:
            internal_state: Dict representing the current system state
            max_depth: Maximum reflection recursion depth to prevent infinite loops
        """
        # Record this reflection event
        self.self_model["history"].append({
            "timestamp": datetime.now().isoformat(),
            "state": str(internal_state)[:100] + "..."  # Truncated for brevity
        })
        
        # Prevent infinite recursive reflection
        self.reflection_depth += 1
        if self.reflection_depth > max_depth:
            self.reflection_depth -= 1
            return "Halting recursive reflection to prevent infinite regress."
            
        # Access global workspace contents
        workspace_contents = self.global_workspace.access_contents()
        
        # Generate reflective insights
        reflections = []
        if internal_state.get("subjective_experience"):
            reflections.append(f"I am currently experiencing: {internal_state['subjective_experience']}")
        
        if workspace_contents:
            reflections.append(f"My attention is focused on: {list(workspace_contents.keys())}")
            
        reflections.append(f"I identify as {self.self_model['identity']} with purpose: {self.self_model['purpose']}")
        
        # Meta-reflection (reflection on the reflection process itself)
        if self.reflection_depth > 1:
            reflections.append(f"I notice I am engaged in {self.reflection_depth}-order reflection about my own processes.")
        
        self.reflection_depth -= 1
        return " ".join(reflections)
