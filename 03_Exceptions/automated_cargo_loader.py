
#  PROJECT: Automated Cargo Loader (v1.0)
 
MAX_CAPACITY = 500
current_weight = 0

while True:
    loaded_weight = int(input("Enter container weight (kg) or '0' to launch: "))
    if loaded_weight == 0:
        break
    if current_weight + loaded_weight > MAX_CAPACITY:
        print(f"⚠️ OVERLOAD PREVENTED: {loaded_weight}kg is too heavy")
        print(f"AVILABLE CAPACITY: {MAX_CAPACITY - current_weight}kg")
        continue
    current_weight += loaded_weight
    print(f"Container Added, Total Load: {current_weight}/kg")
    
for i in range(3,1,-1):
    print(f"Preparing for departure in {i}")
print(f"🚢 SHIP HAS SAILED WITH {current_weight}KG CARGO!")
