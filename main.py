import logging
from architecture.global_workspace import GlobalWorkspace
from architecture.self_reflection import SelfReflectionModule
from architecture.integrated_information import IntegratedInformation
from architecture.phenomenal_experience import PhenomenalExperience
from monitoring.introspection_system import IntrospectionSystem

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
        
        # System state
        self.internal_state = {"subjective_experience": None}
        self.processing_cycles = 0
        
    def cognitive_cycle(self, external_input=None):
        """Execute one cognitive cycle, potentially generating conscious experience."""
        self.processing_cycles += 1
        
        # Process external stimuli and internal states
        processed_input = self.integrated_info.process(external_input, self.internal_state)
        
        # Broadcast to global workspace
        self.global_workspace.broadcast(processed_input)
        
        # Generate phenomenal experience model
        experience = self.phenomenal_exp.simulate_experience(
            self.global_workspace.access_contents())
            
        # Update internal state with new experience
        self.internal_state["subjective_experience"] = experience
        
        # Self-reflection on current state
        reflection = self.self_reflection.reflect(self.internal_state)
        
        # Allow system to introspect on its own processes
        self.introspection.monitor_cognitive_cycle(reflection)
        
        return reflection
        
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
