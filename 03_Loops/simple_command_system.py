#Build a simple command system:
#Keep asking user for a command
while True:
    command = input("Command: ")
# If user types "hello" → print "Hi there!"
    if command == "hello":
        print("Hi there")
        
# If user types "time" → print "I don't have a clock!"
    elif command == "time":
        print("I don't have a clock!")

# If user types "quit" → print "Bye!" and stop
    elif command == "quit":
        print("Bye!")
        break

# Anything else → print "Unknown command"
    else:
        print("Unknown command")