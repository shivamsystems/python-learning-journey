##exercise - bigger number
n1 = float(input("Enter 1st number: "))
n2 = float(input("Enter 2nd number: "))
n3 = float(input("Enter 3rd number: "))

if n1 > n2:
    if n1 > n3:
        print(f"{n1} is the largest number")
    else:
        print(f"{n3} is the largest number")

elif n1 < n2:
    if n2 > n3:
        print(f"{n2} is the largest number")
    else:
        print(f"{n3} is the largest number")

else:
    print("All numbers are same")
    