numbers = [10, 25, 3, -5, 8, -2, 7]
total = 0 
for num in numbers:
    
    if num < 0:
        continue
    total += num 
    print(num, end=", ")
    print(total)
