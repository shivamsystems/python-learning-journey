
#Build a movie ticket price system
#Ask for age

age = float(input("Enter age: "))

#Add: Ask "Weekend? (yes/no)"

weekend = input("Is today weekend ? (Yes/No): ").lower().strip()

#Child (0-12): 100₹
if 12 >= age > 0:
    payment = 100

#Teen (13-17): 150₹  
elif 17 >= age >= 13:
   payment = 150
    
#Adult (18-59): 200₹
elif 59 >= age >= 18:
    payment = 200
    
#Senior (60+): 120₹
elif 100 > age > 60:
    payment = 120
    
else:
    print("Please enter the currect values")
    
#Add 50₹ extra
if weekend == "yes":
    payment = payment + 50
print(f"Please pay {payment}")







