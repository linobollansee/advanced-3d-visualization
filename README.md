# Advanced 3D Visualization Suite | Fortgeschrittene 3D-Visualisierungs-Suite

[English](#english) | [Deutsch](#deutsch)

---

<a name="english"></a>
## 🇬🇧 English

Professional-grade 3D graphics and visualization suite using PyVista, Plotly, and advanced rendering techniques. This project demonstrates complex 3D rendering capabilities including volumetric data, parametric surfaces, fluid dynamics simulations, and interactive visualizations.

### Features

🧠 **Volumetric Brain Scan** - Medical-grade volumetric rendering with sigmoid opacity mapping  
📐 **Parametric Surfaces** - Klein bottle with physically-based rendering (PBR)  
🌊 **Fluid Dynamics Simulation** - Real-time streamline visualization with vortex flow  
⚛️ **Quantum Visualization** - Electron probability density with nested isosurfaces  
🤖 **Interactive Neural Network** - 3D deep learning architecture with Plotly  
🏔️ **Fractal Landscape** - Diamond-square algorithm for procedural terrain generation

### Requirements

- Python 3.8 or higher
- Windows/Linux/macOS
- ~500MB disk space for dependencies

### Quick Start

#### Option 1: Using the QuickStart Script (Windows)

Simply run the PowerShell script:

```powershell
.\quickstart.ps1
```

This script will:
- ✓ Check for Python installation
- ✓ Create a virtual environment
- ✓ Install all dependencies
- ✓ Launch the application

#### Option 2: Manual Installation

1. **Create a virtual environment** (recommended):
   ```powershell
   python -m venv venv
   ```

2. **Activate the virtual environment**:
   - Windows PowerShell:
     ```powershell
     .\venv\Scripts\Activate.ps1
     ```
   - Windows Command Prompt:
     ```cmd
     venv\Scripts\activate.bat
     ```
   - Linux/macOS:
     ```bash
     source venv/bin/activate
     ```

3. **Install dependencies**:
   ```powershell
   pip install -r requirements.txt
   ```

4. **Run the application**:
   ```powershell
   python advanced_3d_visualization.py
   ```

### Usage

When you run the application, you'll see an interactive menu:

```
Select visualization:
1. Volumetric Brain Scan (Medical Imaging)
2. Parametric Surface with PBR (Klein Bottle)
3. Fluid Dynamics Simulation
4. Quantum Orbital Visualization
5. Interactive Neural Network
6. Fractal Landscape
7. Run All Visualizations

Enter choice (1-7):
```

### Dependencies

- **PyVista** (>=0.44.0) - 3D visualization and mesh analysis
- **Plotly** (>=5.24.0) - Interactive 3D plotting
- **NumPy** (>=1.26.0) - Numerical computing
- **SciPy** (>=1.14.0) - Scientific computing utilities

### Technical Highlights

- **Volume Rendering**: Sigmoid opacity transfer functions for realistic depth perception
- **Parametric Surfaces**: Vectorized Klein bottle equations with self-intersection handling
- **Fluid Dynamics**: Streamline integration through 3D vector fields
- **Quantum Mechanics**: Hydrogen orbital probability density with marching cubes isosurfaces
- **Fractal Generation**: Diamond-square algorithm with adjustable roughness parameter
- **PBR Materials**: Physically-based rendering with metallic and roughness properties

### Troubleshooting

**"Python not found" error**  
Make sure Python is installed and added to your system PATH. Download from [python.org](https://www.python.org/).

**PowerShell script execution policy error**  
Run: `Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser`

**Display/rendering issues**  
Ensure your graphics drivers are up to date. PyVista requires OpenGL support.

---

<a name="deutsch"></a>
## 🇩🇪 Deutsch

Professionelle 3D-Grafik- und Visualisierungs-Suite mit PyVista, Plotly und fortgeschrittenen Rendering-Techniken. Dieses Projekt demonstriert komplexe 3D-Rendering-Fähigkeiten einschließlich volumetrischer Daten, parametrischer Oberflächen, Strömungsdynamik-Simulationen und interaktiver Visualisierungen.

### Funktionen

🧠 **Volumetrischer Gehirn-Scan** - Medizinisches volumetrisches Rendering mit Sigmoid-Transparenz  
📐 **Parametrische Oberflächen** - Klein-Flasche mit physikalisch-basiertem Rendering (PBR)  
🌊 **Strömungsdynamik-Simulation** - Echtzeit-Stromlinien-Visualisierung mit Wirbelströmung  
⚛️ **Quanten-Visualisierung** - Elektronen-Wahrscheinlichkeitsdichte mit verschachtelten Isoflächen  
🤖 **Interaktives Neuronales Netzwerk** - 3D Deep-Learning-Architektur mit Plotly  
🏔️ **Fraktale Landschaft** - Diamond-Square-Algorithmus für prozedurale Terraingenerierung

### Voraussetzungen

- Python 3.8 oder höher
- Windows/Linux/macOS
- ~500MB Festplattenspeicher für Abhängigkeiten

### Schnellstart

#### Option 1: QuickStart-Skript verwenden (Windows)

Führen Sie einfach das PowerShell-Skript aus:

```powershell
.\quickstart.ps1
```

Dieses Skript wird:
- ✓ Python-Installation überprüfen
- ✓ Virtuelle Umgebung erstellen
- ✓ Alle Abhängigkeiten installieren
- ✓ Anwendung starten

#### Option 2: Manuelle Installation

1. **Virtuelle Umgebung erstellen** (empfohlen):
   ```powershell
   python -m venv venv
   ```

2. **Virtuelle Umgebung aktivieren**:
   - Windows PowerShell:
     ```powershell
     .\venv\Scripts\Activate.ps1
     ```
   - Windows Eingabeaufforderung:
     ```cmd
     venv\Scripts\activate.bat
     ```
   - Linux/macOS:
     ```bash
     source venv/bin/activate
     ```

3. **Abhängigkeiten installieren**:
   ```powershell
   pip install -r requirements.txt
   ```

4. **Anwendung ausführen**:
   ```powershell
   python advanced_3d_visualization.py
   ```

### Verwendung

Beim Start der Anwendung erscheint ein interaktives Menü:

```
Visualisierung auswählen:
1. Volumetrischer Gehirn-Scan (Medizinische Bildgebung)
2. Parametrische Oberfläche mit PBR (Klein-Flasche)
3. Strömungsdynamik-Simulation
4. Quanten-Orbital-Visualisierung
5. Interaktives Neuronales Netzwerk
6. Fraktale Landschaft
7. Alle Visualisierungen ausführen

Auswahl eingeben (1-7):
```

### Abhängigkeiten

- **PyVista** (>=0.44.0) - 3D-Visualisierung und Mesh-Analyse
- **Plotly** (>=5.24.0) - Interaktive 3D-Plots
- **NumPy** (>=1.26.0) - Numerisches Rechnen
- **SciPy** (>=1.14.0) - Wissenschaftliche Rechenwerkzeuge

### Technische Highlights

- **Volumen-Rendering**: Sigmoid-Transparenzfunktionen für realistische Tiefenwahrnehmung
- **Parametrische Oberflächen**: Vektorisierte Klein-Flaschen-Gleichungen mit Selbstdurchdringungs-Behandlung
- **Strömungsdynamik**: Stromlinie-Integration durch 3D-Vektorfelder
- **Quantenmechanik**: Wasserstoff-Orbital-Wahrscheinlichkeitsdichte mit Marching-Cubes-Isoflächen
- **Fraktal-Generierung**: Diamond-Square-Algorithmus mit einstellbarem Rauheitsparameter
- **PBR-Materialien**: Physikalisch-basiertes Rendering mit Metall- und Rauheitseigenschaften

### Fehlerbehebung

**"Python nicht gefunden"-Fehler**  
Stellen Sie sicher, dass Python installiert und zum System-PATH hinzugefügt ist. Download von [python.org](https://www.python.org/).

**PowerShell-Skript Ausführungsrichtlinie-Fehler**  
Ausführen: `Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser`

**Anzeige-/Rendering-Probleme**  
Stellen Sie sicher, dass Ihre Grafiktreiber aktuell sind. PyVista benötigt OpenGL-Unterstützung.

---

## Project Structure | Projektstruktur

```
advanced-3d-visualization/
├── advanced_3d_visualization.py  # Main application | Hauptanwendung
├── requirements.txt              # Python dependencies | Python-Abhängigkeiten
├── quickstart.ps1               # Windows quickstart | Windows-Schnellstart
├── README.md                    # This file | Diese Datei
└── venv/                        # Virtual environment | Virtuelle Umgebung
```

## License | Lizenz

This project is provided as-is for educational and demonstration purposes.  
Dieses Projekt wird wie besehen für Bildungs- und Demonstrationszwecke bereitgestellt.

---

**Enjoy exploring 3D visualizations! | Viel Spaß beim Erkunden von 3D-Visualisierungen! 🚀**
