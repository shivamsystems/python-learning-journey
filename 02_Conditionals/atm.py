#exercise - ATM
balance = 1000

print("=== ATM ===")
print("1. Check Balance")
print("2. Deposit")
print("3. Withdraw")

choice = int(input("Please input the option: "))

if choice == 1:
    print(f"Your balance after deposit is {balance}₹")
    
elif choice == 2:
    y = int(input("Enter the ammount: "))
    balance = balance + y
    print(f"Your final balance is {balance}₹")
    
elif choice == 3:
    withdrawal_ammount = int(input("Enter the ammount: "))
    balance = balance - withdrawal_ammount
    if balance > 0:
        print(f"Your final ammount after Withdrawal is {balance} ")
    else:
        print(f"Enter ammount greater than {choice}")
 
    