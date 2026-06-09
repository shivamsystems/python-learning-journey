'''
Combine Exercises 1 and 2. Ask for distance, time, and calculate speed.
Use one try block, but catch BOTH ValueError (if they type letters)
and ZeroDivisionError (if time is 0) using separate except blocks.
Print different error messages for each.
'''
try:
    robot_id = int(input("Robot ID (Interger): "))
    distance = float(input("Distance(m): "))
    time = float(input("Time(s): "))
    speed = distance/time
    print(f"Speed of Robot_{robot_id}: {speed:.2f}m/s")
except ZeroDivisionError:
    print("Time cannot be zero")
except ValueError:
    print("Distance & Time should be a number")

