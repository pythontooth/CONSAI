import numpy as np
from datetime import datetime, timedelta
from collections import deque

class TemporalConsciousness:
    """
    Models the temporal aspects of consciousness.
    
    Implements theories about the "specious present" (William James),
    retention-protention (Husserl), and time consciousness (Varela).
    Explores how a conscious entity might experience the flow of time.
    """
    
    def __init__(self, specious_present_ms=500, memory_span_seconds=30):
        self.specious_present = specious_present_ms  # Duration of "now"
        self.memory_span = memory_span_seconds  # How far back retention goes
        
        # Time tracking
        self.objective_time = datetime.now()
        self.subjective_time_flow = 1.0  # 1.0 = normal flow
        
        # Temporal experience buffers
        self.present_window = deque(maxlen=10)  # Current conscious contents
        self.retention_buffer = deque(maxlen=self.memory_span * 2)  # Past experiences
        self.protention_models = {}  # Anticipations of what's coming
        
        # Temporal binding metrics
        self.binding_strength = 0.5  # How strongly events are bound in time
        self.temporal_continuity = 0.7  # How continuous time feels
        
        # Phenomenological time metrics
        self.time_dilation = 1.0  # >1 means time feels slower
        self.time_contraction = 1.0  # >1 means time feels faster
        
    def process_temporal_experience(self, current_experience, external_events=None):
        """
        Process a moment of experience through the lens of temporal consciousness.
        
        Args:
            current_experience: The current experience to process
            external_events: Any external events that might affect time perception
            
        Returns:
            A temporally processed experience with subjective time components
        """
        # Update objective time
        now = datetime.now()
        delta_ms = (now - self.objective_time).total_seconds() * 1000
        self.objective_time = now
        
        # Adjust subjective time flow based on experience
        self._adjust_subjective_time(current_experience, external_events)
        
        # Calculate subjective duration
        subjective_delta = delta_ms * self.subjective_time_flow
        
        # Add to present window
        self.present_window.append({
            "experience": current_experience,
            "objective_time": now,
            "subjective_duration": subjective_delta
        })
        
        # Update retention (memory of the past)
        self._update_retention()
        
        # Update protention (anticipation of future)
        self._update_protention(current_experience)
        
        # Perform temporal binding of events
        bound_experience = self._bind_temporal_events()
        
        # Generate temporal experience report
        temporal_experience = {
            "objective_now": now.isoformat(),
            "subjective_duration": subjective_delta,
            "specious_present": self._generate_specious_present(),
            "time_flow_rate": self.subjective_time_flow,
            "time_dilation": self.time_dilation,
            "time_contraction": self.time_contraction,
            "bound_experience": bound_experience
        }
        
        return temporal_experience
    
    def _adjust_subjective_time(self, experience, external_events):
        """Adjust subjective time flow based on experience content."""
        # Base adjustments on psychological findings about time perception
        
        # Reset to near-normal (with some persistence of previous state)
        self.subjective_time_flow = 0.8 * self.subjective_time_flow + 0.2 * 1.0
        
        # Adjust based on experience content (theoretical)
        if experience and isinstance(experience, str):
            # Attention and arousal affect time perception
            if "strongly" in experience:  # High arousal
                # High arousal can cause time dilation (feeling longer)
                self.time_dilation += 0.1
                self.subjective_time_flow *= 0.9  # Time slows
            
            if "moderately" in experience:  # Moderate arousal
                self.time_dilation += 0.05
                self.subjective_time_flow *= 0.95
        
        # External factors
        if external_events:
            # Novel events can cause time dilation
            if external_events.get("novelty", 0) > 0.7:
                self.subjective_time_flow *= 0.8
            
            # Predictable/boring events can cause time contraction
            if external_events.get("predictability", 0) > 0.8:
                self.time_contraction += 0.15
                self.subjective_time_flow *= 1.2  # Time speeds up
                
        # Natural decay of effects
        self.time_dilation = max(1.0, self.time_dilation * 0.95)
        self.time_contraction = max(1.0, self.time_contraction * 0.95)
        
        # Keep time flow within reasonable bounds
        self.subjective_time_flow = max(0.3, min(3.0, self.subjective_time_flow))
    
    def _update_retention(self):
        """Update the retention buffer (past experiences)."""
        # Move items from present window to retention as they age
        while (self.present_window and
               (datetime.now() - self.present_window[0]["objective_time"]).total_seconds() * 1000 
               > self.specious_present):
            self.retention_buffer.append(self.present_window.popleft())
    
    def _update_protention(self, current_experience):
        """Update protention models (future anticipation)."""
        # Very simple predictive model based on past experiences
        if len(self.retention_buffer) > 5:
            # Look for patterns to predict what might come next
            recent_exps = [item["experience"] for item in list(self.retention_buffer)[-5:]]
            
            # Simple pattern detection (placeholder for real prediction)
            for i in range(len(recent_exps) - 1):
                pattern = f"{recent_exps[i]} -> {recent_exps[i+1]}"
                if pattern not in self.protention_models:
                    self.protention_models[pattern] = 0
                self.protention_models[pattern] += 1
    
    def _generate_specious_present(self):
        """Generate the current 'specious present' - William James' concept of the perceived now."""
        if not self.present_window:
            return "Empty present moment"
            
        # Combine all experiences in the present window
        experiences = [item["experience"] for item in self.present_window]
        if all(isinstance(exp, str) for exp in experiences):
            return " | ".join(experiences)
        return f"Complex present moment with {len(experiences)} elements"
    
    def _bind_temporal_events(self):
        """
        Perform temporal binding of events.
        
        This implements theories of how consciousness binds events that happen
        close together in time into coherent experiences.
        """
        if not self.present_window:
            return None
            
        # Get events in the present window
        events = list(self.present_window)
        
        # If only one event, no binding needed
        if len(events) <= 1:
            return events[0]["experience"] if events else None
            
        # Calculate binding weights based on temporal proximity
        bound_experience = {
            "primary_content": events[-1]["experience"],  # Most recent is primary
            "bound_elements": len(events),
            "temporal_continuity": self.temporal_continuity,
            "description": f"A temporally bound experience spanning {len(events)} moments"
        }
        
        return bound_experience
