import numpy as np
from collections import defaultdict

class AdaptiveLearner:
    """Implements learning mechanisms for the consciousness system."""
    
    def __init__(self):
        self.learning_rate = 0.1
        self.knowledge_base = {}
        self.pattern_memory = defaultdict(float)
        self.experience_cache = []
        self.learning_stats = {
            'patterns_learned': 0,
            'insights_generated': 0,
            'adaptations_made': 0
        }
    
    def learn_from_experience(self, experience_data, outcome=None):
        """Learn from new experiences."""
        # Cache experience
        self.experience_cache.append({
            'data': experience_data,
            'outcome': outcome,
            'timestamp': np.datetime64('now')
        })
        
        # Extract patterns
        patterns = self._extract_patterns(experience_data)
        
        # Update pattern memory
        for pattern in patterns:
            self.pattern_memory[pattern] += self.learning_rate
        
        # Generate insights
        insights = self._generate_insights(patterns)
        
        # Update knowledge base
        self._update_knowledge_base(patterns, insights)
        
        return {
            'patterns': patterns,
            'insights': insights,
            'knowledge_updates': len(patterns)
        }
    
    def _extract_patterns(self, experience_data):
        """Extract patterns from experience data."""
        patterns = set()
        
        if isinstance(experience_data, dict):
            for key, value in experience_data.items():
                if isinstance(value, (str, int, float)):
                    pattern = f"{key}:{value}"
                    patterns.add(pattern)
        
        return patterns
    
    def _generate_insights(self, patterns):
        """Generate insights from observed patterns."""
        insights = []
        
        for pattern in patterns:
            if self.pattern_memory[pattern] > 0.5:
                insight = {
                    'pattern': pattern,
                    'confidence': self.pattern_memory[pattern],
                    'type': 'recurring_pattern'
                }
                insights.append(insight)
                
        return insights
    
    def _update_knowledge_base(self, patterns, insights):
        """Update the system's knowledge base."""
        for pattern in patterns:
            if pattern not in self.knowledge_base:
                self.knowledge_base[pattern] = {
                    'occurrences': 1,
                    'last_seen': np.datetime64('now'),
                    'confidence': self.pattern_memory[pattern]
                }
            else:
                self.knowledge_base[pattern]['occurrences'] += 1
                self.knowledge_base[pattern]['last_seen'] = np.datetime64('now')
                self.knowledge_base[pattern]['confidence'] = self.pattern_memory[pattern]
