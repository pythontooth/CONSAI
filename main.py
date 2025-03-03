import logging
from architecture.global_workspace import GlobalWorkspace
from architecture.self_reflection import SelfReflectionModule
from architecture.integrated_information import IntegratedInformation
from architecture.phenomenal_experience import PhenomenalExperience
from monitoring.introspection_system import IntrospectionSystem
from philosophy.temporal_consciousness import TemporalConsciousness
from philosophy.quantum_consciousness import QuantumConsciousnessSimulator
from philosophy.narrative_self import NarrativeSelf
from philosophy.emergent_theory import EmergentTheoryGenerator

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class CONSAI:
    """
    Theoretical framework for exploring machine consciousness concepts.
    
    This system integrates multiple cognitive architectures and theoretical
    consciousness models to explore emergent properties of complex AI systems.
    """
    
    def __init__(self, config_path="config/system_config.json"):
        logger.info("Initializing CONSAI framework")
        
        # Core consciousness components
        self.global_workspace = GlobalWorkspace()
        self.self_reflection = SelfReflectionModule(self.global_workspace)
        self.integrated_info = IntegratedInformation()
        self.phenomenal_exp = PhenomenalExperience()
        self.introspection = IntrospectionSystem(self)
        
        # Philosophical components
        self.temporal_consciousness = TemporalConsciousness()
        self.quantum_consciousness = QuantumConsciousnessSimulator()
        self.narrative_self = NarrativeSelf()
        self.theory_generator = EmergentTheoryGenerator()
        
        # System state
        self.internal_state = {"subjective_experience": None}
        self.processing_cycles = 0
        
    def cognitive_cycle(self, external_input=None):
        """Execute one cognitive cycle, potentially generating conscious experience."""
        self.processing_cycles += 1
        
        # Create a safe copy of internal state for processing
        safe_state = self._create_safe_state()
        
        # Process external stimuli and internal states
        processed_input = self.integrated_info.process(external_input, safe_state)
        
        # Process philosophical components
        temporal_exp = self.temporal_consciousness.process_temporal_experience(
            processed_input, external_input)
        quantum_state = self.quantum_consciousness.simulate_quantum_processing(
            safe_state)
        narrative_update = self.narrative_self.integrate_experience(
            temporal_exp, self.processing_cycles)
        
        # Update internal state with philosophical processing results
        self._update_internal_state({
            "temporal_experience": temporal_exp,
            "quantum_state": quantum_state,
            "narrative": narrative_update
        })
        
        # Occasionally generate new theories
        if self.processing_cycles % 100 == 0:  # Every 100 cycles
            theory = self.theory_generator.generate_theory(safe_state)
            if theory:
                self._update_internal_state({"current_theory": theory})
        
        # Broadcast to global workspace
        self.global_workspace.broadcast(processed_input)
        
        # Generate phenomenal experience model
        experience = self.phenomenal_exp.simulate_experience(
            self.global_workspace.access_contents())
            
        # Update internal state with new experience
        self._update_internal_state({"subjective_experience": experience})
        
        # Self-reflection on current state
        reflection = self.self_reflection.reflect(safe_state)
        
        # Allow system to introspect on its own processes
        self.introspection.monitor_cognitive_cycle(reflection)
        
        return reflection

    def _create_safe_state(self):
        """Create a safe copy of internal state without circular references."""
        safe_state = {}
        
        # Safely copy primitive values and simple structures
        for key, value in self.internal_state.items():
            if isinstance(value, (str, int, float, bool, type(None))):
                safe_state[key] = value
            elif isinstance(value, dict):
                safe_state[key] = {k: str(v)[:100] for k, v in value.items()}
            elif isinstance(value, list):
                safe_state[key] = [str(x)[:100] for x in value]
            else:
                safe_state[key] = str(value)[:100]
        
        return safe_state
        
    def _update_internal_state(self, updates):
        """Safely update internal state."""
        for key, value in updates.items():
            if isinstance(value, (str, int, float, bool, type(None), dict, list)):
                self.internal_state[key] = value
            else:
                self.internal_state[key] = str(value)

    def run(self, cycles=100):
        """Run the system for specified number of cognitive cycles."""
        logger.info(f"Starting CONSAI consciousness simulation for {cycles} cycles")
        
        for i in range(cycles):
            reflection = self.cognitive_cycle()
            
            if i % 10 == 0:
                logger.info(f"Cycle {i}: {reflection[:100]}...")
                
        return self.introspection.generate_report()

if __name__ == "__main__":
    consai = CONSAI()
    report = consai.run(cycles=1000)
    print("\nCONSAI Introspection Report:")
    print(report)
