"""
Advanced 3D Visualization Suite
Professional-grade graphics using PyVista, Matplotlib, and Plotly
Demonstrates complex 3D rendering, volumetric data, and interactive visualizations
"""

import numpy as np
import pyvista as pv
from pyvista import examples
import plotly.graph_objects as go
from scipy.spatial import Delaunay
import colorsys

class Professional3DGraphics:
    """High-end 3D graphics generator using professional visualization libraries"""
    
    def __init__(self):
        self.plotter = None
        
    def create_volumetric_brain_scan(self):
        """Create a professional medical-grade volumetric rendering"""
        print("Generating volumetric brain scan visualization...")
        
        # Create plotter with professional settings
        plotter = pv.Plotter(window_size=[1920, 1080], off_screen=False)
        
        # Load example brain data (high-resolution medical imaging)
        volume = examples.download_brain()
        
        # Apply advanced volume rendering with opacity mapping
        # Sigmoid opacity creates smooth transparency transitions for better depth perception
        # EN: Applies volumetric rendering with sigmoid opacity function for realistic depth
        # DE: Wendet volumetrisches Rendering mit Sigmoid-Transparenzfunktion für realistische Tiefe an
        plotter.add_volume(
            volume,
            cmap="bone",
            opacity="sigmoid",  # Smooth opacity gradient / Glatter Transparenzverlauf
            shade=True,
            ambient=0.2,
            diffuse=0.7,
            specular=0.3,
            specular_power=15,
        )
        
        # Add professional lighting
        plotter.add_light(pv.Light(position=(10, 10, 10), light_type='scene light'))
        plotter.add_light(pv.Light(position=(-10, -10, 10), light_type='scene light', intensity=0.5))
        
        plotter.camera_position = 'xz'
        plotter.background_color = '#1a1a1a'
        plotter.show(title="Volumetric Brain Scan - Medical Grade Rendering")
        
    def create_parametric_surface(self):
        """Generate complex parametric surface with PBR materials"""
        print("Creating parametric surface with PBR materials...")
        
        plotter = pv.Plotter(window_size=[1920, 1080])
        
        # Create a complex parametric surface (Klein bottle)
        def klein_bottle(u, v):
            u = u * 2 * np.pi
            v = v * 2 * np.pi
            r = 4 * (1 - np.cos(u) / 2)
            
            # EN: np.where performs vectorized conditionals - crucial for performance with large arrays
            # DE: np.where führt vektorisierte Bedingungen aus - entscheidend für Performance bei großen Arrays
            # Klein bottle parametric equations split at u=π for self-intersection handling
            # Klein-Flasche parametrische Gleichungen geteilt bei u=π für Selbstdurchdringung
            x = np.where(
                u < np.pi,
                6 * np.cos(u) * (1 + np.sin(u)) + r * np.cos(u) * np.cos(v),
                6 * np.cos(u) * (1 + np.sin(u)) + r * np.cos(v + np.pi)
            )
            
            y = np.where(
                u < np.pi,
                16 * np.sin(u) + r * np.sin(u) * np.cos(v),
                16 * np.sin(u)
            )
            
            z = r * np.sin(v)
            return x, y, z
        
        # Generate mesh
        u = np.linspace(0, 1, 200)
        v = np.linspace(0, 1, 200)
        U, V = np.meshgrid(u, v)
        
        X, Y, Z = klein_bottle(U.flatten(), V.flatten())
        points = np.column_stack((X, Y, Z))
        
        # EN: Delaunay triangulation creates optimal surface mesh from point cloud
        # DE: Delaunay-Triangulation erstellt optimales Oberflächennetz aus Punktwolke
        cloud = pv.PolyData(points)
        surface = cloud.delaunay_2d()  # 2D Delaunay in parameter space / 2D Delaunay im Parameterraum
        
        # Apply physically-based rendering
        plotter.add_mesh(
            surface,
            color='#FF6B35',
            pbr=True,
            metallic=0.8,
            roughness=0.2,
            smooth_shading=True,
        )
        
        # Professional lighting setup
        plotter.add_light(pv.Light(position=(20, 20, 20), light_type='scene light', intensity=1.0))
        plotter.add_light(pv.Light(position=(-20, -20, 20), light_type='scene light', intensity=0.6))
        plotter.add_light(pv.Light(position=(0, 0, 50), light_type='scene light', intensity=0.3))
        
        plotter.background_color = '#0a0a0a'
        plotter.enable_anti_aliasing('ssaa')
        plotter.show(title="Klein Bottle - Parametric Surface with PBR")
        
    def create_fluid_dynamics_simulation(self):
        """Create a fluid dynamics visualization using streamlines"""
        print("Simulating fluid dynamics with streamlines...")
        
        # Generate vector field for fluid flow
        x = np.arange(-10, 10, 0.5)
        y = np.arange(-10, 10, 0.5)
        z = np.arange(-5, 5, 0.5)
        X, Y, Z = np.meshgrid(x, y, z)
        
        # Create complex vector field (simulating vortex flow)
        r = np.sqrt(X**2 + Y**2)
        theta = np.arctan2(Y, X)
        
        U = -np.sin(theta) * np.exp(-r/10) - Z/20
        V = np.cos(theta) * np.exp(-r/10) + X/30
        W = np.sin(r/5) * np.cos(Z/3) * 0.5
        
        # Create grid
        grid = pv.StructuredGrid(X, Y, Z)
        grid['vectors'] = np.column_stack((U.flatten(), V.flatten(), W.flatten()))
        
        # Create streamlines
        plotter = pv.Plotter(window_size=[1920, 1080])
        
        # EN: Streamlines trace particle paths through vector field using numerical integration
        # DE: Stromlinien verfolgen Partikelpfade durch Vektorfeld mittels numerischer Integration
        seed_points = pv.PolyData(np.random.uniform(-8, 8, (50, 3)))
        streamlines = grid.streamlines_from_source(
            seed_points,
            vectors='vectors',
            max_time=100,  # Integration time steps / Integrationszeitschritte
            integration_direction='both'  # Forward and backward / Vorwärts und rückwärts
        )
        
        # EN: Compute velocity magnitude from vector components using L2 norm
        # DE: Berechnet Geschwindigkeitsbetrag aus Vektorkomponenten mit L2-Norm
        streamlines['velocity'] = np.linalg.norm(
            streamlines['vectors'], axis=1
        )
        
        plotter.add_mesh(
            streamlines.tube(radius=0.1),
            scalars='velocity',
            cmap='plasma',
            smooth_shading=True,
            pbr=True,
            metallic=0.5,
            roughness=0.3,
        )
        
        # Add boundary sphere
        sphere = pv.Sphere(radius=12, theta_resolution=60, phi_resolution=60)
        plotter.add_mesh(
            sphere,
            color='#1a1a1a',
            opacity=0.1,
            style='wireframe',
        )
        
        plotter.add_light(pv.Light(position=(30, 30, 30)))
        plotter.background_color = '#000000'
        plotter.enable_anti_aliasing('ssaa')
        plotter.show(title="Fluid Dynamics - Vortex Flow Simulation")
        
    def create_quantum_visualization(self):
        """Visualize quantum probability density using isosurfaces"""
        print("Creating quantum orbital visualization...")
        
        # Create hydrogen orbital probability density
        n, l, m = 4, 2, 0  # 4d orbital
        
        # Create grid
        x = np.linspace(-20, 20, 150)
        y = np.linspace(-20, 20, 150)
        z = np.linspace(-20, 20, 150)
        X, Y, Z = np.meshgrid(x, y, z)
        
        # EN: Convert Cartesian to spherical coordinates for quantum wavefunction calculation
        # DE: Wandelt kartesische in sphärische Koordinaten für Quantenwellenfunktion-Berechnung um
        r = np.sqrt(X**2 + Y**2 + Z**2)
        theta = np.arccos(np.clip(Z / (r + 1e-10), -1, 1))  # Clip prevents arccos domain errors / Verhindert arccos-Bereichsfehler
        phi = np.arctan2(Y, X)
        
        # EN: Simplified hydrogen wavefunction (real orbitals use Laguerre/Legendre polynomials)
        # DE: Vereinfachte Wasserstoff-Wellenfunktion (echte Orbitale nutzen Laguerre/Legendre-Polynome)
        R = (r**(l)) * np.exp(-r/(2*n)) * np.cos(m * phi)  # Radial part / Radialer Teil
        Y_lm = np.sin(theta)**abs(m) * np.cos(l * theta)  # Angular part / Winkelabhängiger Teil
        psi = R * Y_lm  # Complete wavefunction / Vollständige Wellenfunktion
        
        # Probability density
        prob = np.abs(psi)**2
        
        # Create volume
        grid = pv.StructuredGrid(X, Y, Z)
        grid['probability'] = prob.flatten()
        
        plotter = pv.Plotter(window_size=[1920, 1080])
        
        # EN: Create nested isosurfaces at 70th, 80th, 90th percentiles to show probability shells
        # DE: Erstellt verschachtelte Isoflächen bei 70., 80., 90. Perzentil für Wahrscheinlichkeitsschalen
        levels = np.percentile(prob[prob > 0], [70, 80, 90])
        
        for i, level in enumerate(levels):
            contour = grid.contour([level], scalars='probability')  # Marching cubes algorithm / Marching-Cubes-Algorithmus
            opacity = 0.3 + (i * 0.2)  # Increasing opacity for inner shells / Steigende Transparenz für innere Schalen
            color = colorsys.hsv_to_rgb(i * 0.15, 0.8, 1.0)  # HSV to RGB color mapping / HSV zu RGB Farbzuordnung
            
            plotter.add_mesh(
                contour,
                color=color,
                opacity=opacity,
                smooth_shading=True,
                pbr=True,
                metallic=0.3,
                roughness=0.4,
            )
        
        # Add nucleus representation
        nucleus = pv.Sphere(radius=0.5, center=(0, 0, 0))
        plotter.add_mesh(nucleus, color='white', emissive=True)
        
        plotter.add_light(pv.Light(position=(40, 40, 40), intensity=0.8))
        plotter.add_light(pv.Light(position=(-40, -40, 40), intensity=0.4))
        plotter.background_color = '#000000'
        plotter.enable_anti_aliasing('ssaa')
        plotter.show(title="Quantum Orbital - Electron Probability Density")
        
    def create_interactive_neural_network(self):
        """Create an interactive 3D neural network visualization with Plotly"""
        print("Generating interactive neural network architecture...")
        
        # Define network architecture
        layers = [8, 16, 32, 16, 4]
        
        # Generate node positions
        nodes_x, nodes_y, nodes_z = [], [], []
        node_colors = []
        node_sizes = []
        
        for layer_idx, num_nodes in enumerate(layers):
            x = layer_idx * 3
            angle_step = 2 * np.pi / num_nodes
            radius = num_nodes * 0.3
            
            for node_idx in range(num_nodes):
                angle = node_idx * angle_step
                y = radius * np.cos(angle)
                z = radius * np.sin(angle)
                
                nodes_x.append(x)
                nodes_y.append(y)
                nodes_z.append(z)
                
                # Color based on layer
                hue = layer_idx / len(layers)
                color = colorsys.hsv_to_rgb(hue, 0.8, 1.0)
                node_colors.append(f'rgb({int(color[0]*255)}, {int(color[1]*255)}, {int(color[2]*255)})')
                node_sizes.append(8 + layer_idx * 2)
        
        # Generate connections
        edge_x, edge_y, edge_z = [], [], []
        node_idx = 0
        
        for layer_idx in range(len(layers) - 1):
            current_layer_size = layers[layer_idx]
            next_layer_size = layers[layer_idx + 1]
            
            for i in range(current_layer_size):
                for j in range(next_layer_size):
                    current_node = node_idx + i
                    next_node = node_idx + current_layer_size + j
                    
                    edge_x.extend([nodes_x[current_node], nodes_x[next_node], None])
                    edge_y.extend([nodes_y[current_node], nodes_y[next_node], None])
                    edge_z.extend([nodes_z[current_node], nodes_z[next_node], None])
            
            node_idx += current_layer_size
        
        # Create edge trace
        edge_trace = go.Scatter3d(
            x=edge_x, y=edge_y, z=edge_z,
            mode='lines',
            line=dict(color='rgba(100, 100, 255, 0.15)', width=1),
            hoverinfo='none',
            name='Connections'
        )
        
        # Create node trace
        node_trace = go.Scatter3d(
            x=nodes_x, y=nodes_y, z=nodes_z,
            mode='markers',
            marker=dict(
                size=node_sizes,
                color=node_colors,
                line=dict(color='white', width=0.5),
                opacity=0.9
            ),
            text=[f'Layer {i//sum(1 for _ in layers)}, Node {i%10}' for i in range(len(nodes_x))],
            hoverinfo='text',
            name='Neurons'
        )
        
        # Create figure
        fig = go.Figure(data=[edge_trace, node_trace])
        
        fig.update_layout(
            title=dict(
                text='Deep Neural Network Architecture - Interactive 3D',
                font=dict(size=24, color='white')
            ),
            scene=dict(
                xaxis=dict(showgrid=False, showticklabels=False, title=''),
                yaxis=dict(showgrid=False, showticklabels=False, title=''),
                zaxis=dict(showgrid=False, showticklabels=False, title=''),
                bgcolor='rgb(10, 10, 10)',
            ),
            paper_bgcolor='rgb(20, 20, 20)',
            plot_bgcolor='rgb(10, 10, 10)',
            showlegend=False,
            width=1920,
            height=1080,
        )
        
        fig.show()
        
    def create_fractal_landscape(self):
        """Generate a stunning fractal landscape with advanced lighting"""
        print("Generating fractal terrain landscape...")
        
        def diamond_square(size, roughness=0.7):
            """EN: Diamond-square algorithm for procedural terrain generation
               DE: Diamond-Square-Algorithmus für prozedurale Terraingenerierung"""
            n = 2**size + 1  # Grid size must be 2^n + 1 / Gittergröße muss 2^n + 1 sein
            terrain = np.zeros((n, n))
            
            # Initialize corners with random values / Ecken mit Zufallswerten initialisieren
            terrain[0, 0] = np.random.randn()
            terrain[0, -1] = np.random.randn()
            terrain[-1, 0] = np.random.randn()
            terrain[-1, -1] = np.random.randn()
            
            step_size = n - 1
            scale = 1.0  # Noise amplitude / Rauschamplitude
            
            while step_size > 1:
                half_step = step_size // 2
                
                # EN: Diamond step - average square corners and add randomness
                # DE: Diamond-Schritt - Quadratecken mitteln und Zufälligkeit hinzufügen
                for i in range(0, n-1, step_size):
                    for j in range(0, n-1, step_size):
                        avg = (terrain[i, j] + terrain[i, j+step_size] +
                               terrain[i+step_size, j] + terrain[i+step_size, j+step_size]) / 4
                        terrain[i+half_step, j+half_step] = avg + np.random.randn() * scale
                
                # Square step
                for i in range(0, n, half_step):
                    for j in range((i + half_step) % step_size, n, step_size):
                        count = 0
                        total = 0
                        
                        if i >= half_step:
                            total += terrain[i-half_step, j]
                            count += 1
                        if i + half_step < n:
                            total += terrain[i+half_step, j]
                            count += 1
                        if j >= half_step:
                            total += terrain[i, j-half_step]
                            count += 1
                        if j + half_step < n:
                            total += terrain[i, j+half_step]
                            count += 1
                        
                        terrain[i, j] = total / count + np.random.randn() * scale
                
                step_size = half_step
                scale *= roughness
            
            return terrain
        
        # Generate terrain
        terrain = diamond_square(8, roughness=0.6)
        
        # Create mesh
        x = np.linspace(0, 100, terrain.shape[0])
        y = np.linspace(0, 100, terrain.shape[1])
        X, Y = np.meshgrid(x, y)
        
        # Scale height
        Z = terrain * 20
        
        # Create surface
        grid = pv.StructuredGrid(X, Y, Z)
        
        # Add elevation as scalar
        grid['elevation'] = Z.flatten()
        
        plotter = pv.Plotter(window_size=[1920, 1080])
        
        # Add terrain with custom colormap
        plotter.add_mesh(
            grid,
            scalars='elevation',
            cmap='gist_earth',
            smooth_shading=True,
            pbr=True,
            metallic=0.1,
            roughness=0.8,
            show_scalar_bar=False,
        )
        
        # Add atmospheric lighting
        plotter.add_light(pv.Light(position=(50, 50, 100), light_type='scene light', intensity=1.2))
        plotter.add_light(pv.Light(position=(-50, 50, 50), light_type='scene light', intensity=0.3, color='#FFD700'))
        
        # Add fog effect with gradient background
        plotter.background_color = '#87CEEB'
        plotter.camera_position = [(150, 150, 80), (50, 50, 0), (0, 0, 1)]
        plotter.enable_anti_aliasing('ssaa')
        
        plotter.show(title="Fractal Landscape - Procedurally Generated Terrain")


def main():
    """Run all professional visualization demonstrations"""
    print("=" * 70)
    print("PROFESSIONAL 3D GRAPHICS VISUALIZATION SUITE")
    print("Using PyVista, Plotly, and NumPy/SciPy")
    print("=" * 70)
    print()
    
    graphics = Professional3DGraphics()
    
    # Menu
    print("Select visualization:")
    print("1. Volumetric Brain Scan (Medical Imaging)")
    print("2. Parametric Surface with PBR (Klein Bottle)")
    print("3. Fluid Dynamics Simulation")
    print("4. Quantum Orbital Visualization")
    print("5. Interactive Neural Network")
    print("6. Fractal Landscape")
    print("7. Run All Visualizations")
    print()
    
    choice = input("Enter choice (1-7): ").strip()
    
    visualizations = {
        '1': graphics.create_volumetric_brain_scan,
        '2': graphics.create_parametric_surface,
        '3': graphics.create_fluid_dynamics_simulation,
        '4': graphics.create_quantum_visualization,
        '5': graphics.create_interactive_neural_network,
        '6': graphics.create_fractal_landscape,
    }
    
    if choice == '7':
        for viz in visualizations.values():
            viz()
            print("\n" + "="*70 + "\n")
    elif choice in visualizations:
        visualizations[choice]()
    else:
        print("Invalid choice. Running Neural Network visualization as default...")
        graphics.create_interactive_neural_network()
    
    print("\nVisualization complete!")


if __name__ == "__main__":
    main()
