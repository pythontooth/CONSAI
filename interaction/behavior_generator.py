import numpy as np
from collections import OrderedDict

class BehaviorGenerator:
    """Generates behaviors based on internal states and external context."""
    
    def __init__(self):
        self.behavior_repertoire = OrderedDict({
            'explore': self._explore_behavior,
            'respond': self._response_behavior,
            'learn': self._learning_behavior,
            'rest': self._rest_behavior
        })
        self.current_behavior = None
        self.behavior_history = []
        
    def generate_behavior(self, internal_state, external_context):
        """Generate appropriate behavior based on current state."""
        # Calculate behavior scores
        behavior_scores = {}
        for behavior_name in self.behavior_repertoire:
            score = self._evaluate_behavior_fit(
                behavior_name, internal_state, external_context)
            behavior_scores[behavior_name] = score
        
        # Select behavior with highest score
        selected_behavior = max(behavior_scores.items(), key=lambda x: x[1])[0]
        
        # Generate behavior
        behavior = self.behavior_repertoire[selected_behavior](
            internal_state, external_context)
        
        # Record history
        self.current_behavior = behavior
        self.behavior_history.append({
            'behavior': selected_behavior,
            'score': behavior_scores[selected_behavior],
            'context': str(external_context)[:100]
        })
        
        return behavior
    
    def _evaluate_behavior_fit(self, behavior_name, internal_state, context):
        """Evaluate how appropriate a behavior is for current situation."""
        base_score = np.random.uniform(0.3, 0.7)
        
        # Add context-specific scoring
        if context.get('requires_response') and behavior_name == 'respond':
            base_score += 0.3
        elif context.get('novel_stimulus') and behavior_name == 'explore':
            base_score += 0.3
        elif internal_state.get('learning_opportunity') and behavior_name == 'learn':
            base_score += 0.3
            
        return min(1.0, base_score)
    
    def _explore_behavior(self, internal_state, context):
        """Generate exploratory behavior."""
        return {
            'type': 'explore',
            'action': 'investigate_environment',
            'parameters': {'scope': 'broad', 'intensity': 0.7}
        }
    
    def _response_behavior(self, internal_state, context):
        """Generate response behavior."""
        return {
            'type': 'respond',
            'action': 'generate_response',
            'parameters': {'mode': 'adaptive', 'intensity': 0.8}
        }
    
    def _learning_behavior(self, internal_state, context):
        """Generate learning behavior."""
        return {
            'type': 'learn',
            'action': 'acquire_knowledge',
            'parameters': {'focus': 'current_context', 'intensity': 0.9}
        }
    
    def _rest_behavior(self, internal_state, context):
        """Generate rest behavior."""
        return {
            'type': 'rest',
            'action': 'conserve_resources',
            'parameters': {'duration': 'short', 'intensity': 0.3}
        }
