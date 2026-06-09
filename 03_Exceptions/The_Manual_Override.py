while True:
    try:
        length = float(input("Arm Extension Length (cm): "))
        if length > 200:
            raise ValueError("Extension exceeds physical limits!")
    except ValueError:
        print("Extension exceeds physical limits!")
    else:
        print(f"Attention!, Arm extended to {length} cm")
        break
    finally:
        print("Restarting the machine for safety")
