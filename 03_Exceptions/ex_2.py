'''
Write a script that asks for distance and time.
Calculate speed = distance / time.
Catch the ZeroDivisionError if the user enters 0 for time,
and print "Time cannot be zero."
'''
while True:
    try:
        distance = float(input("Distance(m): "))
        time = float(input("Time(s): "))
        speed = distance/time
    except ZeroDivisionError:
        print("Time cannot be zero")
    except ValueError:
        print("Distance & Time should be a number")
    else:
        print(f"Speed: {speed:.2f} m/s")
        break
    finally:
        for i in range(4,0,-1):
            print(f"Shutting down the system to prevent the error in {i} sec...")
