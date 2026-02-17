def main():
    # Demonstrating the difference between Assignment (=) and Comparison (==)
    target_reps = 10
    current_reps = 0
    
    is_workout_complete = False  # Boolean flag

    print("Starting workout loop...")

    # A While Loop checking a Boolean condition
    while not is_workout_complete:
        current_reps += 1  # Incrementing
        
        # Using Conditional Logic
        if current_reps == target_reps: # Comparison operator
            print(f"Rep {current_reps}: Target hit!")
            is_workout_complete = True # Update Boolean
        else:
            print(f"Rep {current_reps}: Push harder...")

    print("Workout complete. Logic verified.")

main()
