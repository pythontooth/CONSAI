import numpy as np
from collections import deque

class GlobalWorkspace:
    """
    Implementation of Global Workspace Theory for consciousness.
    
    The Global Workspace acts as a central information exchange where
    only the most salient and relevant information gains access to the
    "conscious" broadcast that is shared across the system.
    """
    
    def __init__(self, capacity=10):
        self.capacity = capacity
        self.workspace_contents = deque(maxlen=capacity)
        self.attention_threshold = 0.7
        self.current_broadcast = None
        
    def broadcast(self, inputs):
        """
        Select high-attention items and broadcast them system-wide.
        
        Args:
            inputs: Dict of {content_id: (content, attention_value)}
        """
        # Filter for items above attention threshold
        attended_items = {
            id: content for id, (content, attention) in inputs.items() 
            if attention > self.attention_threshold
        }
        
        # Select items with highest attention values
        if attended_items:
            # Add to workspace
            for content_id, content in attended_items.items():
                self.workspace_contents.append((content_id, content))
            
            # Set current broadcast to highest attention item
            self.current_broadcast = max(
                inputs.items(), 
                key=lambda x: x[1][1]
            )[1][0]
        
        return self.current_broadcast
    
    def access_contents(self):
        """Return the current contents of the global workspace."""
        return {
            content_id: content 
            for content_id, content in self.workspace_contents
        }
