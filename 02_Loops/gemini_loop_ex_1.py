'''
for i in range(5):
    print("Calibrating joint...")

#---------------
battery = 100
while battery >=80:
    print(f"Battery at {battery}% - Operating")
    battery -= 5

print("Battery low. Returning to dock.")

#Roster Check (Easy)
parts = ["Servo", "Motherboard", "Chassis", "Camera"]
for part in parts:
    print(f"COmponent loaded: {part}")

#Evens Only
for i in range(2,13,2):
    print(i, end=",")


while True:
    password = input("Enter a password: ")
    if password == "admin123":
        print("Access Granted")
        break
    else:
        print("Access Denied. Try again.")

for i in range(1,6):
    if i == 3:
        continue
    print(f"Sector {i} successfully scanned")


while True:
    direction = input("Enter a direction(E,S,W,N and q for quit): ")
    if direction == "q":
        break
    else:
        print(f"Moving to direction: {direction}")



for i in range(1,3):
    for j in range(1,3):
        print(f"checking cell: ({i},{j})")
        if i == 2 and j == 2:
            print(f"Target acquired at ({i}, {j})!")
            break

total_payload = 0
while True:
    added_payload = input("Enter item weight (or type 'done' to finish): ").lower().strip()
    if added_payload == "done":
        print(f"Total payload weight: {total_payload} kg")
        break
    total_payload += int(added_payload)
    '''