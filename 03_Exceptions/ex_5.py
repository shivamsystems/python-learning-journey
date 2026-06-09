while True:
    try:
        pressure = float(input("Enter the Hydraulic pressure: "))
    except ValueError:
        print("Don't Enter a text, Enter a number")
        
    else:
        print(f"Pressure set to {pressure}")
        break
