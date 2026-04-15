def set_joint_angle(angle):
    if not (0 <= angle <= 180):
        raise ValueError(f"CRITICAL: Joint angle {angle} violates physical stops!")
    print(f"Moving joint to {angle}°")

try:
    requested_angle = int(input("Angle: ")) 
    set_joint_angle(requested_angle)
except ValueError as e:
    print(f"Safety Logic Triggered > {e}")
