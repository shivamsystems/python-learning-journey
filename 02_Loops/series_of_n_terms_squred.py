total = 0
count = 0
while True:
    num = int(input("Enter a number (0 for final): "))
    if num == 0:
        break
    total += num
    count += 1

if count > 0:
    avg = total / count
    print(f"Sum is {total}, Average is {avg}")
else:
    print("No numbers entered!")