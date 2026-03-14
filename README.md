# Temperature-Controller
A multi-threaded HVAC simulation that models a thermostat state machine with environmental drift and keyboard controls.

## 🌡️ Features
- **Hysteresis Logic**: Prevents system "short-cycling" by requiring a 3-degree temperature variance before activation.
- **Environmental Drift**: Models natural temperature changes toward the outside ambient temperature when the system is idle.
- **Multi-threaded Input**: Uses `pynput` to listen for hardware keyboard events without blocking the main simulation logic.
- **Safety Clamping**: Internal temperature limits (32°F - 105°F) to simulate hardware constraints.

## 🚀 Getting Started

### Prerequisites
- Python 3.8+
- [pynput](https://pypi.org/project/pynput/) library

### Installation
1. Clone the repository:
   ```bash
   git clone [https://github.com/yourusername/thermostat-sim.git](https://github.com/yourusername/thermostat-sim.git)
   cd thermostat-sim
2. Install dependencies:
   ```bash
   pip install pynput

3. Run the simulation:
   ```bash
   python main.py

### Controls
| Key | Action |
|:---:|:---:|
|1|Set Mode to HEATING|
|2|Set Mode to COOLING|
|3|Set Mode to OFF|
|Up Arrow|Increase Target Temperature|
|Down Arrow|Decrese Target Temperature|
|Delete|Safely Exit Simulation|

### 🏗️ Project Structure
- main.py: Entry point that orchestrates the simulation and input threads.
- Thermostat/controller.py: The "Brain" containing the HVAC state logic.
- Thermostat/interface.py: The input handler for keyboard events.
- Thermostat/__init__.py: Package initialization.

### 📝 License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
