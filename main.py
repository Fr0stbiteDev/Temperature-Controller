import time
from pynput import keyboard
from Thermostat import KeyboardInterface, ThermostatController

def main():
    # --- SETUP PHASE ---
    # Initialize the core controller (Model) with a starting ambient temperature
    system = ThermostatController(outside_temp=72)
    
    # Initialize the input handler (View/Controller) and link it to the system
    ui = KeyboardInterface(system, keyboard)
    
    # --- CONCURRENCY SETUP ---
    # The pynput Listener runs in its own background thread.
    # This allows the main loop to process logic while the system waits for key presses.
    listener = keyboard.Listener(on_press=ui.on_press)
    listener.start()

    # --- USER INTERFACE ---
    print("--- Thermostat System Active ---")
    print("Use 1, 2, 3 for Modes | Up/Down for Temp | Delete to Exit")

    # --- MAIN EXECUTION LOOP ---
    # Continues running until the 'disabled' flag is flipped via the UI thread
    while not system.disabled:
        # Step 1: Process the thermostat's internal logic and state changes
        system.update_logic()

        # Step 2: Provide real-time feedback to the console
        print(f"Current: {system.current_temp}°F | Target: {system.target_temp}°F | Mode: {system.mode}")

        # Step 3: Rate-limiting - prevents the loop from consuming 100% CPU
        time.sleep(1)

    # --- CLEANUP PHASE ---
    # Ensure the background thread is closed properly before the program exits
    listener.stop()

if __name__ == "__main__":
    main()