import unittest
import numpy as np
from datetime import datetime
import sys
import os

# Add project root to Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from main import CONSAI

class ConsciousnessTests(unittest.TestCase):
    """Test suite for CONSAI consciousness framework."""
    
    def setUp(self):
        """Set up test environment."""
        self.consai = CONSAI()
        self.test_input = {
            'visual': np.random.rand(10, 10),
            'auditory': np.random.rand(5),
            'timestamp': datetime.now()
        }
    
    def test_integrated_information(self):
        """Test if system generates non-zero phi values."""
        phi = self.consai.integrated_info._calculate_phi()
        self.assertGreater(phi, 0.0)
        self.assertLessEqual(phi, 1.0)
    
    def test_phenomenal_experience(self):
        """Test phenomenal experience generation."""
        experience = self.consai.phenomenal_exp.simulate_experience(
            {'test': 'content'})
        self.assertIsNotNone(experience)
    
    def test_self_reflection(self):
        """Test self-reflection capabilities."""
        reflection = self.consai.self_reflection.reflect(
            {'test': 'state'})
        self.assertIsInstance(reflection, str)
        self.assertGreater(len(reflection), 0)
    
    def test_learning_adaptation(self):
        """Test if system shows learning behavior."""
        initial_state = self.consai.cognitive_cycle()
        # Run multiple cycles
        for _ in range(5):
            new_state = self.consai.cognitive_cycle()
            self.assertNotEqual(initial_state, new_state)
    
    def test_narrative_consistency(self):
        """Test narrative self consistency."""
        narrative1 = self.consai.narrative_self.integrate_experience(
            "test experience", 1)
        narrative2 = self.consai.narrative_self.integrate_experience(
            "test experience", 2)
        self.assertIsNotNone(narrative1)
        self.assertIsNotNone(narrative2)
