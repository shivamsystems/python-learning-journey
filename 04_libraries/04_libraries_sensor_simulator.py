"""
Practice: 04 Libraries
Topic: Using built-in Python libraries (random, time, math)
Goal: Simulate LiDAR and temperature sensor readings for a robotic joint.
"""

import random
import time
import math

def generate_sensor_data(num_samples=5):
    print("Initializing Sensor Diagnostics...")
    data = []
    for i in range(num_samples):
        # Simulating random noise in sensor readings
        temperature = round(random.uniform(40.0, 85.0), 2)  # Motor temp in Celsius
        angle = round(random.uniform(0, 360), 2)            # Joint angle
        
        # Using math library to calculate hypothetical torque based on angle
        torque = round(abs(math.sin(math.radians(angle)) * 10), 2) 
        
        timestamp = time.strftime("%H:%M:%S")
        
        data.append({
            "time": timestamp,
            "temp": temperature,
            "angle": angle,
            "torque": torque
        })
        time.sleep(0.5) # Pausing execution to simulate real-time polling
        
    return data

if __name__ == "__main__":
    readings = generate_sensor_data()
    print("\n--- Diagnostic Results ---")
    for r in readings:
        print(f"[{r['time']}] Temp: {r['temp']}°C | Angle: {r['angle']}° | Torque: {r['torque']} Nm")
