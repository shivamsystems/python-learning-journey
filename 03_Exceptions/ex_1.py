'''
Write a script that asks the user for a robot_id (must be an integer).
Use a try/except block to catch a ValueError.
If an error occurs, print "Invalid ID format."
'''
try:
    robot_id = int(input("Robot ID (Interger): "))
    print(f"Robot ID is {robot_id}") # should i write print inside try or outside try ?
except ValueError:
    print("Invalid ID format")
