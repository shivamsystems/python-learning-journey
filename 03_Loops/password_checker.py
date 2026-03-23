correct = "secret.124"
for attempt in range(1, 4):
    password = input(f"Attempt {attempt}/3 Password:")
    if correct == password:
        print("Access Granted")
        break
else:
    print("Account Blocked")