import tkinter as tk
from tkinter import ttk, scrolledtext
import numpy as np  # Add numpy import
import networkx as nx
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import threading
import queue
import time
import sys
import os

# Add project root to path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from main import CONSAI

class ConsAIGui:
    def __init__(self, root):
        self.root = root
        self.root.title("CONSAI Monitor")
        self.root.geometry("1200x800")
        
        # Initialize CONSAI
        self.consai = CONSAI()
        self.running = False
        self.update_queue = queue.Queue()
        self.input_queue = queue.Queue()  # Add input queue
        
        # Add data buffers
        self.phi_values = []
        self.time_values = []
        self.max_data_points = 100
        
        self._create_gui_elements()
        self._setup_layout()
        
        # Configure plots
        self._setup_plots()
        
    def _create_gui_elements(self):
        # Control Panel
        self.control_frame = ttk.LabelFrame(self.root, text="Control Panel")
        self.start_button = ttk.Button(self.control_frame, text="Start", command=self.start_processing)
        self.stop_button = ttk.Button(self.control_frame, text="Stop", command=self.stop_processing)
        self.cycle_label = ttk.Label(self.control_frame, text="Cycles: 0")
        
        # Add simulation controls
        self.speed_label = ttk.Label(self.control_frame, text="Speed:")
        self.speed_scale = ttk.Scale(self.control_frame, from_=1, to=100, orient=tk.HORIZONTAL)
        self.speed_scale.set(20)  # Default speed
        
        # Add input simulation panel
        self.input_frame = ttk.LabelFrame(self.root, text="Input Simulation")
        self.input_types = ttk.Combobox(self.input_frame, 
            values=["visual", "auditory", "conceptual", "emotional"])
        self.input_intensity = ttk.Scale(self.input_frame, from_=0, to=1, orient=tk.HORIZONTAL)
        self.inject_button = ttk.Button(self.input_frame, text="Inject Input", 
            command=self._inject_input)
        
        # Add state monitoring
        self.monitor_frame = ttk.LabelFrame(self.root, text="System Monitoring")
        self.phi_value_label = ttk.Label(self.monitor_frame, text="Current Phi: 0.0")
        self.awareness_label = ttk.Label(self.monitor_frame, text="Awareness Level: 0.0")
        self.complexity_label = ttk.Label(self.monitor_frame, text="System Complexity: 0")
        
        # Add analysis tools
        self.analysis_frame = ttk.LabelFrame(self.root, text="Analysis Tools")
        self.export_button = ttk.Button(self.analysis_frame, text="Export Data", 
            command=self._export_data)
        self.analyze_button = ttk.Button(self.analysis_frame, text="Analyze Patterns", 
            command=self._analyze_patterns)
        self.reset_button = ttk.Button(self.analysis_frame, text="Reset System", 
            command=self._reset_system)
        
        # Phi Monitor
        self.phi_frame = ttk.LabelFrame(self.root, text="Integration (Phi) Monitor")
        self.phi_figure = Figure(figsize=(6, 2))
        self.phi_plot = self.phi_figure.add_subplot(111)
        self.phi_canvas = FigureCanvasTkAgg(self.phi_figure, self.phi_frame)
        self.phi_values = []
        
        # Experience Display
        self.exp_frame = ttk.LabelFrame(self.root, text="Current Experience")
        self.exp_text = scrolledtext.ScrolledText(self.exp_frame, height=3)
        
        # Network Visualization
        self.network_frame = ttk.LabelFrame(self.root, text="Integration Network")
        self.network_figure = Figure(figsize=(6, 4))
        self.network_plot = self.network_figure.add_subplot(111)
        self.network_canvas = FigureCanvasTkAgg(self.network_figure, self.network_frame)
        
        # System State
        self.state_frame = ttk.LabelFrame(self.root, text="System State")
        self.state_text = scrolledtext.ScrolledText(self.state_frame, height=10)
        
        # Log Display
        self.log_frame = ttk.LabelFrame(self.root, text="System Log")
        self.log_text = scrolledtext.ScrolledText(self.log_frame, height=10)
        
    def _setup_layout(self):
        # Control Panel Layout
        self.control_frame.grid(row=0, column=0, columnspan=2, padx=5, pady=5, sticky="ew")
        self.start_button.pack(side=tk.LEFT, padx=5, pady=5)
        self.stop_button.pack(side=tk.LEFT, padx=5, pady=5)
        self.cycle_label.pack(side=tk.LEFT, padx=5, pady=5)
        
        # Add new controls to control panel
        self.speed_label.pack(side=tk.LEFT, padx=5)
        self.speed_scale.pack(side=tk.LEFT, padx=5)
        
        # Phi Monitor Layout
        self.phi_frame.grid(row=1, column=0, columnspan=2, padx=5, pady=5, sticky="nsew")
        self.phi_canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)
        
        # Input simulation panel layout
        self.input_frame.grid(row=1, column=2, padx=5, pady=5, sticky="nsew")
        self.input_types.pack(padx=5, pady=5)
        self.input_intensity.pack(padx=5, pady=5)
        self.inject_button.pack(padx=5, pady=5)
        
        # Experience Display Layout
        self.exp_frame.grid(row=2, column=0, columnspan=2, padx=5, pady=5, sticky="nsew")
        self.exp_text.pack(fill=tk.BOTH, expand=True)
        
        # Monitoring panel layout
        self.monitor_frame.grid(row=2, column=2, padx=5, pady=5, sticky="nsew")
        self.phi_value_label.pack(padx=5, pady=2)
        self.awareness_label.pack(padx=5, pady=2)
        self.complexity_label.pack(padx=5, pady=2)
        
        # Network and State Layout
        self.network_frame.grid(row=3, column=0, padx=5, pady=5, sticky="nsew")
        self.network_canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)
        self.state_frame.grid(row=3, column=1, padx=5, pady=5, sticky="nsew")
        self.state_text.pack(fill=tk.BOTH, expand=True)
        
        # Analysis tools layout
        self.analysis_frame.grid(row=3, column=2, padx=5, pady=5, sticky="nsew")
        self.export_button.pack(padx=5, pady=2)
        self.analyze_button.pack(padx=5, pady=2)
        self.reset_button.pack(padx=5, pady=2)
        
        # Log Layout
        self.log_frame.grid(row=4, column=0, columnspan=2, padx=5, pady=5, sticky="nsew")
        self.log_text.pack(fill=tk.BOTH, expand=True)
        
        # Configure grid weights
        self.root.grid_rowconfigure(3, weight=1)
        self.root.grid_columnconfigure(0, weight=1)
        self.root.grid_columnconfigure(1, weight=1)
        
    def _setup_plots(self):
        """Initialize plot settings."""
        # Phi plot settings
        self.phi_plot.set_title("Phi Value Over Time")
        self.phi_plot.set_xlabel("Time")
        self.phi_plot.set_ylabel("Phi")
        self.phi_plot.grid(True)
        self.phi_plot.set_ylim(0, 1)
        
        # Network plot settings
        self.network_plot.set_title("Integration Network")
        
        # Initial draw
        self.phi_canvas.draw()
        self.network_canvas.draw()

    def start_processing(self):
        if not self.running:
            self.running = True
            threading.Thread(target=self._processing_loop, daemon=True).start()
            self.root.after(100, self._update_gui)
            
    def stop_processing(self):
        self.running = False
        # Clean shutdown
        time.sleep(0.1)
        self.update_queue.queue.clear()
        
    def _processing_loop(self):
        try:
            while self.running:
                # Get current speed setting and convert to delay
                speed = self.speed_scale.get()
                delay = 1.0 / speed  # Convert speed (1-100) to delay (1.0-0.01 seconds)
                
                # Run one cognitive cycle
                reflection = self.consai.cognitive_cycle()
                phi = self.consai.integrated_info._calculate_phi()
                network = self.consai.integrated_info.network
                
                # Process any pending inputs
                while not self.input_queue.empty():
                    input_data = self.input_queue.get()
                    if input_data['type'] == 'input':
                        reflection = self.consai.cognitive_cycle(input_data['data'])
                
                # Queue update if GUI still running
                if self.running:
                    self.update_queue.put({
                        'cycles': self.consai.processing_cycles,
                        'phi': phi,
                        'experience': reflection,
                        'network': network,
                        'state': self.consai.internal_state
                    })
                
                time.sleep(delay)  # Use dynamic delay based on speed
        except Exception as e:
            print(f"Processing error: {e}")
            self.running = False
            
    def _update_gui(self):
        try:
            start_time = time.time()
            updates_processed = 0
            
            # Process all queued updates, but limit time spent
            while not self.update_queue.empty() and updates_processed < 10 and (time.time() - start_time) < 0.1:
                data = self.update_queue.get_nowait()
                self._update_displays(data)
                updates_processed += 1
                
            # Schedule next update if still running
            if self.running:
                self.root.after(50, self._update_gui)
                
        except Exception as e:
            print(f"GUI update error: {e}")
            self.running = False
            
    def _update_displays(self, data):
        """Update all display elements with new data."""
        # Update cycle count
        self.cycle_label.configure(text=f"Cycles: {data['cycles']}")
        
        # Update phi plot
        self.phi_values.append(data['phi'])
        self.time_values.append(data['cycles'])
        if len(self.phi_values) > self.max_data_points:
            self.phi_values.pop(0)
            self.time_values.pop(0)
            
        self.phi_plot.clear()
        self.phi_plot.plot(self.time_values, self.phi_values, 'b-')
        self.phi_plot.set_ylim(0, 1)
        self.phi_plot.grid(True)
        self.phi_canvas.draw_idle()
        
        # Update experience text
        self.exp_text.delete('1.0', tk.END)
        self.exp_text.insert(tk.END, data['experience'])
        
        # Update network visualization (less frequently)
        if data['cycles'] % 5 == 0:  # Update every 5 cycles
            self.network_plot.clear()
            pos = nx.spring_layout(data['network'])
            nx.draw(data['network'], pos, ax=self.network_plot, 
                   node_color='lightblue', 
                   node_size=500, 
                   with_labels=True,
                   font_size=8)
            self.network_canvas.draw_idle()
        
        # Update state display
        self.state_text.delete('1.0', tk.END)
        for key, value in data['state'].items():
            self.state_text.insert(tk.END, f"{key}: {str(value)[:50]}...\n")
        
        # Add to log and auto-scroll
        self.log_text.insert(tk.END, f"Cycle {data['cycles']}: Phi = {data['phi']:.2f}\n")
        self.log_text.see(tk.END)
        
        # Update monitoring labels
        self.phi_value_label.configure(text=f"Current Phi: {data['phi']:.3f}")
        network_size = len(data['network'])
        self.complexity_label.configure(text=f"System Complexity: {network_size}")
        
        # Calculate awareness level (simplified metric)
        awareness = (data['phi'] + len(data['network']) / 50) / 2
        self.awareness_label.configure(text=f"Awareness Level: {awareness:.3f}")

    def _inject_input(self):
        """Inject simulated input into the system."""
        input_type = self.input_types.get()
        intensity = self.input_intensity.get()
        
        if not input_type:
            return
            
        # Create richer input data based on type
        simulated_input = {
            input_type: {
                'data': self._generate_input_data(input_type, intensity),
                'intensity': intensity,
                'timestamp': time.time()
            }
        }
        
        # Queue the input for processing
        self.input_queue.put({
            'type': 'input',
            'data': simulated_input
        })
        
        # Log the input
        self.log_text.insert(tk.END, f"Injected {input_type} input with intensity {intensity:.2f}\n")
        self.log_text.see(tk.END)

    def _generate_input_data(self, input_type, intensity):
        """Generate more meaningful input data based on type."""
        if input_type == 'visual':
            # Generate a simple pattern (e.g., a shape)
            size = 10
            data = np.zeros((size, size))
            center = size // 2
            radius = int(size * 0.3 * intensity)
            for i in range(size):
                for j in range(size):
                    if (i - center)**2 + (j - center)**2 < radius**2:
                        data[i, j] = intensity
            return data
            
        elif input_type == 'auditory':
            # Generate a simple waveform
            duration = 100
            frequency = 10 * intensity
            time_points = np.linspace(0, 1, duration)
            return intensity * np.sin(2 * np.pi * frequency * time_points)
            
        elif input_type == 'conceptual':
            # Generate abstract concepts with varying complexity
            concepts = {
                'abstraction_level': intensity,
                'complexity': np.random.uniform(0, intensity),
                'clarity': intensity,
                'associations': int(5 * intensity)
            }
            return concepts
            
        elif input_type == 'emotional':
            # Generate emotional input with valence and arousal
            emotions = {
                'valence': np.random.uniform(-1, 1) * intensity,
                'arousal': intensity,
                'dominance': np.random.uniform(0, 1) * intensity
            }
            return emotions
            
        return np.random.rand(10, 10) * intensity  # fallback

    def _export_data(self):
        """Export system data to CSV."""
        import csv
        from datetime import datetime
        
        filename = f"consai_data_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"
        
        with open(filename, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['Cycle', 'Phi', 'Experience', 'Network Size'])
            
            for i, (phi, t) in enumerate(zip(self.phi_values, self.time_values)):
                writer.writerow([t, phi, '', ''])

    def _analyze_patterns(self):
        """Analyze system patterns and display results."""
        if len(self.phi_values) < 10:
            return
            
        # Calculate basic statistics
        avg_phi = np.mean(self.phi_values)
        std_phi = np.std(self.phi_values)
        trend = np.polyfit(range(len(self.phi_values)), self.phi_values, 1)[0]
        
        # Show analysis window
        analysis_window = tk.Toplevel(self.root)
        analysis_window.title("Pattern Analysis")
        
        # Display results
        ttk.Label(analysis_window, 
                 text=f"Average Phi: {avg_phi:.3f}\n" +
                      f"Standard Deviation: {std_phi:.3f}\n" +
                      f"Trend: {'Increasing' if trend > 0 else 'Decreasing'}\n" +
                      f"Stability: {1.0 - std_phi:.3f}").pack(padx=10, pady=10)

    def _reset_system(self):
        """Reset the system to initial state."""
        self.stop_processing()
        self.phi_values = []
        self.time_values = []
        self.consai = CONSAI()
        self._setup_plots()
        self.log_text.delete('1.0', tk.END)
        self.state_text.delete('1.0', tk.END)
        self.exp_text.delete('1.0', tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = ConsAIGui(root)
    root.mainloop()
