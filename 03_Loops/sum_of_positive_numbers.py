#Ask user to keep entering numbers.

total = 0
while True:
    num = int(input("Number: "))
#Ignore negative numbers (use continue).
#Add only positive numbers to total.
    if num < 0:
        continue
#Stop when user enters 0.
#Print the total of positive numbers.
    if num == 0:
        total += num
        print(f"Total Sum is {total}")
        break