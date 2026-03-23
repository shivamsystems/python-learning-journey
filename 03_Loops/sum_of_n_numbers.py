number = int(input("Number: "))
final = 0
for i in range(number + 1):
    final = final + i
    
print(f"Sum of first {number} numbers is {final}")