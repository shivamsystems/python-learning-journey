"""
Practice: 07 Object-Oriented Programming (Classes)
Topic: Creating objects, methods, and managing state
Goal: Model a physical DC Motor as a software object to control its behavior safely.
"""

class DCMotor:
    def __init__(self, name, max_rpm):
        # Attributes defining the state of the motor
        self.name = name
        self.max_rpm = max_rpm
        self.current_rpm = 0
        self.direction = "FORWARD"
        
    def set_speed(self, rpm):
        """Sets the speed, ensuring it doesn't exceed hardware limits."""
        if rpm > self.max_rpm:
            print(f"[{self.name}] WARNING: Requested RPM ({rpm}) exceeds max limit. Capping to {self.max_rpm}.")
            self.current_rpm = self.max_rpm
        elif rpm < 0:
            print(f"[{self.name}] ERROR: RPM cannot be negative. Use reverse() instead.")
            self.current_rpm = 0
        else:
            self.current_rpm = rpm
            
        print(f"[{self.name}] Speed set to {self.current_rpm} RPM.")
        
    def reverse_direction(self):
        """Toggles the rotation direction."""
        # Must slow down to 0 before reversing to prevent mechanical stress
        if self.current_rpm > 0:
            print(f"[{self.name}] Applying brakes before reversing...")
            self.stop()
            
        self.direction = "REVERSE" if self.direction == "FORWARD" else "FORWARD"
        print(f"[{self.name}] Direction changed to {self.direction}.")
        
    def stop(self):
        """Safely halts the motor."""
        self.current_rpm = 0
        print(f"[{self.name}] Motor halted.")

if __name__ == "__main__":
    # Instantiating two different motors
    drive_motor = DCMotor(name="Left_Drive_Wheel", max_rpm=300)
    arm_motor = DCMotor(name="Robotic_Arm_Joint", max_rpm=50)
    
    print("--- Testing Drive Motor ---")
    drive_motor.set_speed(150)
    drive_motor.set_speed(400) # This should trigger the warning cap
    drive_motor.reverse_direction() # This should apply brakes first
    
    print("\n--- Testing Arm Motor ---")
    arm_motor.set_speed(30)
    arm_motor.stop()
