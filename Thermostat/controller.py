class ThermostatController:
    """
    Manages the core logic and state of an HVAC thermostat system

    Attributes:
        current_temp (int): The current temperature of the room.
        target_temp (int): The user-defined desired temperature.
        outside_temp (int): The baseline temperature the room drifts towards when idle.
        mode (str): Current operating mode ('OFF', 'HEATING', 'COOLING').
        is_running (bool): Internal state indicating if the HVAC unit is actively drawing power.
        disabled (bool): Internal state indicating if the simulation is running or not.
    """
    
    def __init__(self, outside_temp):
        self.current_temp = outside_temp
        self.target_temp = outside_temp
        self.outside_temp = outside_temp
        self.mode = "OFF" # OFF, HEATING, COOLING
        self.is_running = True
        self.disabled = False

    def adjust_temp(self, amount):
        self.current_temp = max(32, min(105, self.current_temp + amount))

    def update_logic(self):
        """
        Calculates the temperature change for a single simulation tick.
        Handles environmental drift, hysteresis activation, and active HVAC cycles.
        """
        # --- IDLE STATE & ENVIRONMENTAL DRIFT ---
        # If the system is OFF or has reached its target, it drifts toward ambient outside temp.
        if self.mode == "OFF" or self.is_running == False:
            if self.current_temp > self.outside_temp:
                self.current_temp -= 1
            elif self.current_temp < self.outside_temp:
                self.current_temp += 1

            # HYSTERESIS: Prevents "Short-Cycling" by requiring a 3-degree variance 
            # before the mechanical system re-engages.
            if abs(self.target_temp - self.current_temp) > 3 and (self.mode == "HEATING" or self.mode == "COOLING"):
                self.is_running = True

        # --- ACTIVE HVAC CYCLES ---
        elif self.mode == "HEATING" and self.is_running == True:
            if self.current_temp < self.target_temp:
                self.adjust_temp(1)
            
            else:
                # Target achieved; enter idle state to save energy.
                self.is_running = False

        # When A/C is COOLING and active
        elif self.mode == "COOLING" and self.is_running == True:
            if self.current_temp > self.target_temp:
                self.adjust_temp(-1)

            else:
                # Target achieved; enter idle state to save energy.
                self.is_running = False