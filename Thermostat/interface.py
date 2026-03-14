class KeyboardInterface:
    """
    Handles hardware input events and translates them into thermostat commands.
    
    Acts as the 'Controller' in a Model-View-Controller (MVC) pattern,
    mapping physical key strikes to state changes in the ThermostatController.
    """

    def __init__(self, controller, keyboard):
        self.controller = controller
        self.keyboard = keyboard
    
    def on_press(self, key):
        """
        Callback triggered by the keyboard listener thread.
        
        Args:
            key: The key object provided by the pynput listener.
        Returns:
            bool: False if the listener should stop (on exit), None otherwise.
        """

        try:
            # Handle Alphanumeric Inputs (Mode Selection)
            if key.char == '1':
                self.controller.mode = "HEATING"
                print("Mode: HEATING")
            elif key.char == '2':
                self.controller.mode = "COOLING"
                print("Mode: COOLING")
            elif key.char == '3':
                self.controller.mode = "OFF"
                print("Mode: OFF")

        except AttributeError:
            # Handle Non-Alphanumeric Special Keys (System Controls)
            # AttributeError occurs when accessing .char on non-character keys (e.g., Arrows).

            if key == self.keyboard.Key.up:
                # Clamp target temperature to safety maximum (105°F)
                self.controller.target_temp = min(105, self.controller.target_temp + 1)
                print(f"Target: {self.controller.target_temp}")
            elif key == self.keyboard.Key.down:
                # Clamp target temperature to safety minimum (32°F)
                self.controller.target_temp = max(32, self.controller.target_temp - 1)
                print(f"Target: {self.controller.target_temp}")
            elif key == self.keyboard.Key.delete:
                # Set termination flag to safely shut down the main simulation loop
                self.controller.disabled = True
                print("Quitting...")
                return False # Stops the pynput listener thread