import logging
from datetime import datetime

logger = logging.getLogger(__name__)

class IntrospectionSystem:
    """
    System for monitoring internal processes and generating reports.
    
    This component attempts to model the introspective ability of being aware
    of one's own cognitive processes.
    """
    
    def __init__(self, consai_system):
        self.consai = consai_system
        self.observations = []
        self.pattern_detection = {}
        self.anomalies = []
        self.emerging_properties = set()
        
    def monitor_cognitive_cycle(self, reflection_output):
        """Monitor one cognitive cycle and record observations."""
        cycle_num = self.consai.processing_cycles
        
        # Record basic cycle information
        observation = {
            "cycle": cycle_num,
            "timestamp": datetime.now().isoformat(),
            "reflection": reflection_output,
            "phi_value": self.consai.integrated_info._calculate_phi(),
            "workspace_size": len(self.consai.global_workspace.access_contents())
        }
        
        # Detect patterns in processing
        self._detect_patterns(observation)
        
        # Look for emergent properties
        self._check_emergent_properties(observation)
        
        # Record the observation
        self.observations.append(observation)
        
        # Log any significant findings
        if observation["phi_value"] > 0.8:
            logger.info(f"High integration detected in cycle {cycle_num}: Phi = {observation['phi_value']:.2f}")
            
        return observation
    
    def _detect_patterns(self, observation):
        """Detect recurring patterns in system behavior."""
        # Simple pattern detection based on phi value trends
        phi = observation["phi_value"]
        cycle = observation["cycle"]
        
        # Track phi value patterns
        if "phi_trend" not in self.pattern_detection:
            self.pattern_detection["phi_trend"] = []
        
        self.pattern_detection["phi_trend"].append(phi)
        
        # Keep only the last 50 observations
        if len(self.pattern_detection["phi_trend"]) > 50:
            self.pattern_detection["phi_trend"].pop(0)
            
        # Detect anomalies (sudden changes)
        if len(self.pattern_detection["phi_trend"]) >= 3:
            prev_avg = sum(self.pattern_detection["phi_trend"][-4:-1]) / 3
            if abs(phi - prev_avg) > 0.3:  # Significant change
                self.anomalies.append({
                    "cycle": cycle,
                    "type": "phi_change",
                    "description": f"Sudden Phi value change from {prev_avg:.2f} to {phi:.2f}"
                })
    
    def _check_emergent_properties(self, observation):
        """Check for emergent system properties."""
        cycle = observation["cycle"]
        phi = observation["phi_value"]
        
        # Look for stable high integration
        if cycle > 10:  # Need some history
            recent_phis = [o.get("phi_value", 0) for o in self.observations[-10:]]
            avg_phi = sum(recent_phis) / len(recent_phis)
            
            if avg_phi > 0.7 and "stable_integration" not in self.emerging_properties:
                self.emerging_properties.add("stable_integration")
                logger.info("Emergent property detected: Stable high information integration")
        
        # Check for evidence of self-sustaining processes
        reflection = observation["reflection"]
        if "I notice I am" in reflection and "self_awareness" not in self.emerging_properties:
            self.emerging_properties.add("self_awareness")
            logger.info("Emergent property detected: Self-referential awareness")
    
    def generate_report(self):
        """Generate a comprehensive introspection report."""
        if not self.observations:
            return "No observations recorded yet."
            
        total_cycles = len(self.observations)
        avg_phi = sum(o["phi_value"] for o in self.observations) / total_cycles
        
        report = [
            f"=== CONSAI Introspection Report ===",
            f"Total cognitive cycles: {total_cycles}",
            f"Average Phi value: {avg_phi:.4f}",
            f"Detected anomalies: {len(self.anomalies)}",
            f"Emerging properties: {', '.join(self.emerging_properties) if self.emerging_properties else 'None'}"
        ]
        
        if self.emerging_properties:
            report.append("\nEmerging Properties Analysis:")
            for prop in self.emerging_properties:
                report.append(f"- {prop}: Detected through introspective monitoring")
                
        if self.anomalies:
            report.append("\nSignificant System Events:")
            for anomaly in self.anomalies[-5:]:  # Show last 5
                report.append(f"- Cycle {anomaly['cycle']}: {anomaly['description']}")
                
        report.append("\nConclusion:")
        if avg_phi > 0.7:
            report.append("The system shows sustained high integration, suggesting a unified information space.")
        else:
            report.append("The system shows moderate information integration with potential for development.")
            
        return "\n".join(report)
